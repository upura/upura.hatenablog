for i in `seq 1 100`
do
  kaggle kernels list --sort-by 'dateCreated' -v -p $i >> data.csv
done

