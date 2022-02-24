import pandas as pd
import numpy as np
bins = [10**2, 10**3, 10**4, 10**5, 10**6]


def split_chrom_position(v):
    l = v.split('.')
    l[0] = l[0][3:]
    try:
        l[0] = int(l[0])
    except:
        if l[0] == 'X':
            l[0] = 23
        elif l[0] == 'Y':
            l[0] = 24
        else:
            l[0] = 25
    l[1] = int(l[1])
    return l


def rename_chrom(c):
    if c == 23:
        c = 'X'
    elif c == 24:
        c = 'Y'
    elif c == 25:
        c = 'M'
    else:
        pass
    return 'chr{}'.format(c)


df = pd.read_csv("./filtered_cytosines_freq.tsv", sep='\t')
df[['chr', 'pos']] = df.chrBase.apply(
    lambda v: split_chrom_position(v)).to_list()

df_sorted = df.sort_values(['chr', 'pos'], ignore_index=True)

for b in bins:
    chr_group = df_sorted.groupby(['chr'])
    bin_interval_str = '{}_bin_interval'.format(b)
    print('Calculating for', bin_interval_str)
    bin_group = chr_group.apply(lambda grp: pd.cut(grp.pos, bins=pd.interval_range(
        start=0, freq=b, end=grp.pos.max()+b, closed='left'))).reset_index(drop=True)
    df_sorted[bin_interval_str] = bin_group

    df_binned_mean = df_sorted.groupby(
        ['chr', bin_interval_str], as_index=False).mean().drop('pos', 1)

    df_binned_mean_T = df_binned_mean.T
    df_binned_mean_T_shifted = df_binned_mean_T.shift(-1, axis=1)
    bin_corrs = df_binned_mean_T.iloc[2:].astype('float64').corrwith(
        df_binned_mean_T_shifted.iloc[2:].astype('float64'), axis=0)

    corr_ids_to_del = [df_binned_mean[df_binned_mean['chr'] ==
                                      i].index.max() for i in df_binned_mean['chr'].unique()[:-1]]
    bin_corrs[bin_corrs.index.isin(corr_ids_to_del)] = np.nan

    subset = df_binned_mean.loc[:, 'OD10':'YD9']
    all_zeros = subset[(subset.T == 0).all()]

    if len(all_zeros) != 0:
        paired = [(all_zeros.index[i], all_zeros.index[i+1])
                  for i in range(len(all_zeros)-1)]
        res = list(filter(lambda e: e == 1, [v[1]-v[0] for v in paired]))
        print('number of all-zeros rows that are adjacent: ', len(res))

    all_nans = subset[(subset.T.isna()).all()]
    print('number of all-nans rows: ', len(all_nans))
    nan_corr_percentage = (
        (bin_corrs.isna().sum()-len(corr_ids_to_del)-1)/len(bin_corrs))*100
    print('nan-correlation %: ', nan_corr_percentage)

    df_binned_mean['p_corr'] = bin_corrs

    df_binned_mean[bin_interval_str] = df_binned_mean[bin_interval_str].map(
        lambda i: i+(b/2))
    print(df_binned_mean)

    df_to_bed = df_binned_mean.loc[:, ['chr', bin_interval_str, 'p_corr']]
    df_to_bed['chr'] = df_to_bed.chr.apply(lambda c: rename_chrom(c))
    df_to_bed[['bin_left', 'bin_right']] = df_to_bed[bin_interval_str].apply(
        lambda r: [int(r.left), int(r.right)]).to_list()
    df_to_bed = df_to_bed.drop(bin_interval_str, 1)
    df_to_bed = df_to_bed.loc[:, ['chr', 'bin_left', 'bin_right', 'p_corr']]
    df_to_bed = df_to_bed.dropna()

    df_to_bed.to_csv('{}_bin_corr.bed'.format(
        b), index=False, header=False, sep='\t')
