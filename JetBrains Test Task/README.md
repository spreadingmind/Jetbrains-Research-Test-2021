### Инструкция

- Для просмотра примера всех вычислений (до генерации bed файлов включетельно) с комментариями по и выводами посмотрите `1000_bin_example.ipynb`.

- Для выполнения всего задания запустите bash скрипт `pipeline.sh`. Для генерации bigWig файлов также необходима утилита `bedGraphToBigWig` и файл `hg19.chrom.sizes`, взятые с ресурса http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64.v385/ и из инструкции https://genomebrowser.wustl.edu/goldenPath/help/bigWig.html

- Ссылки на запаблишенные bigWig трэки для загрузки кастомных треков в геномный браузер http://genome.ucsc.edu/:
https://github.com/spreadingmind/python_data_analysis_2021/blob/proj/metilation/100_bin_BigWig.bw?raw=true
https://github.com/spreadingmind/python_data_analysis_2021/blob/proj/metilation/1000_bin_BigWig.bw?raw=true
https://github.com/spreadingmind/python_data_analysis_2021/blob/proj/metilation/10000_bin_BigWig.bw?raw=true
https://github.com/spreadingmind/python_data_analysis_2021/blob/proj/metilation/100000_bin_BigWig.bw?raw=true
https://github.com/spreadingmind/python_data_analysis_2021/blob/proj/metilation/1000000_bin_BigWig.bw?raw=true

    Уже сгенерированные треки также приложены в папке.

- Ccылка на геномный браузер со всеми уже загруженными треками для просмотра: http://genome.ucsc.edu/cgi-bin/hgTracks?db=hg19&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chr1%3A188995464%2D198295859&hgsid=1094004127_7mSxONK1O5hsDa6qsd5tAAVo4Oyz

### Комментарии

1) Комментарии решения приведены для каждого шага в `1000_bin_example.ipynb`

2) Для размеров бинов 100 000 и 1 000 000 последние бины хромосом выходят за границу хромосомы. Поэтому пришлось изменить длины хромосом в `hg19.chrom.sizes` со стандартных на концы полученных сдвинутых бинов. Это хак, так как эти позиции не соответствуют реальным размерам хромосом, но ввиду последнего пункта задания пришлось реализовать так. Как второй вариант можно было бы для этих размеров бинов изменить последний шаг со сдвигом, и не сдвигать полностью последний бин.

3) Так как определение соседних бинов не было оговорено в задании, соседними бинами в решении я считаю любые 2 идущих бина, которые имеются в данных, то есть они могут находиться как непосредственно рядом, так и на расстоянии. Считаю это более целесообразным, чем отбрасывать бины, которые не непосредственно соседние, так как это дает нам данные о зависимости корреляции метилирования от расстояния между бинами, например как в этих статьях:

    https://link.springer.com/content/pdf/10.1186/s13059-015-0581-9.pdf
    https://www.sciencedirect.com/science/article/abs/pii/S0888754319300175

4) Я не работала с bed/big файлами, поэтому не уверена, насколько близко к желаемому выглядят полученные мною треки. Но ввиду ограниченной документации и конечного времени реализовала самый простой вариант, как следующие шаги можно было бы оформить треки подробнее/красивее, лучше разобравшись в работе с ними и с геномным браузером.







