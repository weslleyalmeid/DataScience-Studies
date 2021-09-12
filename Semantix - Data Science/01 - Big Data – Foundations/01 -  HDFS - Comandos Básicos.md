Criar diretórios
```bash
 hdfs dfs -mkdir -p user/aluno/weslley/data/recover/delete
```

Enviar arquivos Local/HDFS
```bash
hdfs dfs -put /input/exercises-data/escola user/aluno/weslley/data
hdfs dfs -put /input/exercises-data/entrada1.txt user/aluno/weslley/data
```


Pegar arquivos HDFS/Local
```bash
hdfs dfs -get user/aluno/weslley/data/escola/alunos.json input/
```


Mover arquivos HDFS/HDFS
```bash
hdfs dfs -mv user/aluno/weslley/data/entrada1.txt user/aluno/weslley/data/recover/
```


Remover diretório
```bash
hdfs dfs -rm -r user/aluno/weslley/data/recover/
```

Remover diretório permanentemente
```bash
hdfs dfs -rm -skipTrash -R user/aluno/weslley/data/recover/delete
```

Localizar arquivo
```bash
hdfs dfs -find /user/ -name "alunos.csv" -print
```


Mostrar último 1KB
```bash
hdfs dfs -tail -f user/aluno/weslley/data/escola/alunos.csv
```

Mostrar 2 primeiras linhas
```bash
hdfs dfs -cat user/aluno/weslley/data/escola/alunos.csv | head -n 2
```


Verificação de soma
```bash
hdfs dfs -checksum user/aluno/weslley/data/escola/alunos.csv
```


Criando arquivo
```bash
hdfs dfs -touchz user/aluno/weslley/data/test
```


Alterando o fator de replicação
```bash
hdfs dfs -setrep 2 user/aluno/weslley/data/test
```


Mostrar informação dos alunos
```bash
hdfs dfs -stat %r user/aluno/weslley/data/escola/alunos.csv
```


Mostrar espaço livre do disco
```bash
hdfs dfs -df -h user/aluno/weslley/data
```

Mostrar uso do disco
```bash
hdfs dfs -du -h user/aluno/weslley/data
```