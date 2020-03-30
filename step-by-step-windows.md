AVISO: alguns anti-vírus e Software de segurança de banco podem interferir na instalação.
As vezes remover o Warsaw, Software do Banco do Brasil, resolve. As vezes uma verão mais antiga do miniconda pode funcionar. Para maiores informações cheque:

 https://github.com/ContinuumIO/anaconda-issues/issues/6258

a) clique no arquivo baixado `Miniconda3-latest-Windows-x86_64.exe` e clique em *Next*;

![](images/win/01-miniconda-install.png?raw=true)


b) escolha *Just Me*;

![](images/win/02-miniconda-justme.png?raw=true)


c) clique em *Agree* na licença (mas só após ler tudo ;-p);

![](images/win/03-miniconda-license.png?raw=true)


d) aceite o diretório padrão;

![](images/win/04-miniconda-directory.png?raw=true)


e) desmarque ambas caixas, pois não queremos o Python do miniconda como padrão e não precisamos colocar o *Miniconda3* no **PATH**;

![](images/win/05-miniconda-boxes.png?raw=true)

f) no final da instalação clique em *Next* e *Finish*;

![](images/win/06-miniconda-final-1.png?raw=true)
![](images/win/07-miniconda-final-2.png?raw=true)


g) procure o ícone *Anaconda Prompt (miniconda3)* e clique nele para certificar que a instalação correu corretamente.

![](images/win/08-miniconda-prompt.png?raw=true)

Para confirmar se o ``conda`` está corretamente instalado digite:

```shell
where conda
```

você dever ver algo assim:

![](images/win/09-miniconda-terminal.png?raw=true)