Criar diretórios
```
 hdfs dfs -mkdir -p user/aluno/weslley/data/recover/delete
```

Enviar arquivos Local/HDFS
```
hdfs dfs -put /input/exercises-data/escola user/aluno/weslley/data
hdfs dfs -put /input/exercises-data/entrada1.txt user/aluno/weslley/data
```


Pegar arquivos HDFS/Local
```
hdfs dfs -get user/aluno/weslley/data/escola/alunos.json input/
```


Mover arquivos HDFS/HDFS
```
hdfs dfs -mv user/aluno/weslley/data/entrada1.txt user/aluno/weslley/data/recover/
```


Remover diretório
```
hdfs dfs -rm -r user/aluno/weslley/data/recover/
```

Remover diretório permanentemente
```
hdfs dfs -rm -skipTrash -R user/aluno/weslley/data/recover/delete
```

Localizar arquivo
```
hdfs dfs -find /user/ -name "alunos.csv" -print
```


Mostrar último 1KB
```
hdfs dfs -tail -f user/aluno/weslley/data/escola/alunos.csv
```

Mostrar 2 primeiras linhas
```
hdfs dfs -cat user/aluno/weslley/data/escola/alunos.csv | head -n 2
```


Verificação de soma
```
hdfs dfs -checksum user/aluno/weslley/data/escola/alunos.csv
```


Criando arquivo
```
hdfs dfs -touchz user/aluno/weslley/data/test
```


Alterando o fator de replicação
```
hdfs dfs -setrep 2 user/aluno/weslley/data/test
```


Mostrar informação dos alunos
```
hdfs dfs -stat %r user/aluno/weslley/data/escola/alunos.csv
```


Mostrar espaço livre do disco
```
hdfs dfs -df -h user/aluno/weslley/data
```

Mostrar uso do disco
```
hdfs dfs -du -h user/aluno/weslley/data
```