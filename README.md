# Aulas de Python durante a quarentena

| Status                                                                                      |
| ------------------------------------------------------------------------------------------- |
| ![Tests](https://github.com/ocefpaf/pyrantine/actions/workflows/linux-tests.yml/badge.svg)  |
| ![Tests](https://github.com/ocefpaf/pyrantine/actions/workflows/osx-tests.yml/badge.svg)    |
| ![Tests](https://github.com/ocefpaf/pyrantine/actions/workflows/win-tests.yml/badge.svg)    |

## Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ocefpaf/pyrantine/master)

[![Binder](https://img.shields.io/badge/pangeo-binder-2F7651.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFkAAABZCAMAAABi1XidAAAB8lBMVEX///9XmsrmZYH1olJXmsr1olJXmsrmZYH1olJXmsr1olJXmsrmZYH1olL1olJXmsr1olJXmsrmZYH1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olJXmsrmZYH1olL1olL0nFf1olJXmsrmZYH1olJXmsq8dZb1olJXmsrmZYH1olJXmspXmspXmsr1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olLeaIVXmsrmZYH1olL1olL1olJXmsrmZYH1olLna31Xmsr1olJXmsr1olJXmsrmZYH1olLqoVr1olJXmsr1olJXmsrmZYH1olL1olKkfaPobXvviGabgadXmsqThKuofKHmZ4Dobnr1olJXmsr1olJXmspXmsr1olJXmsrfZ4TuhWn1olL1olJXmsqBi7X1olJXmspZmslbmMhbmsdemsVfl8ZgmsNim8Jpk8F0m7R4m7F5nLB6jbh7jbiDirOEibOGnKaMhq+PnaCVg6qWg6qegKaff6WhnpKofKGtnomxeZy3noG6dZi+n3vCcpPDcpPGn3bLb4/Mb47UbIrVa4rYoGjdaIbeaIXhoWHmZYHobXvpcHjqdHXreHLroVrsfG/uhGnuh2bwj2Hxk17yl1vzmljzm1j0nlX1olL3AJXWAAAAbXRSTlMAEBAQHx8gICAuLjAwMDw9PUBAQEpQUFBXV1hgYGBkcHBwcXl8gICAgoiIkJCQlJicnJ2goKCmqK+wsLC4usDAwMjP0NDQ1NbW3Nzg4ODi5+3v8PDw8/T09PX29vb39/f5+fr7+/z8/Pz9/v7+zczCxgAABC5JREFUeAHN1ul3k0UUBvCb1CTVpmpaitAGSLSpSuKCLWpbTKNJFGlcSMAFF63iUmRccNG6gLbuxkXU66JAUef/9LSpmXnyLr3T5AO/rzl5zj137p136BISy44fKJXuGN/d19PUfYeO67Znqtf2KH33Id1psXoFdW30sPZ1sMvs2D060AHqws4FHeJojLZqnw53cmfvg+XR8mC0OEjuxrXEkX5ydeVJLVIlV0e10PXk5k7dYeHu7Cj1j+49uKg7uLU61tGLw1lq27ugQYlclHC4bgv7VQ+TAyj5Zc/UjsPvs1sd5cWryWObtvWT2EPa4rtnWW3JkpjggEpbOsPr7F7EyNewtpBIslA7p43HCsnwooXTEc3UmPmCNn5lrqTJxy6nRmcavGZVt/3Da2pD5NHvsOHJCrdc1G2r3DITpU7yic7w/7Rxnjc0kt5GC4djiv2Sz3Fb2iEZg41/ddsFDoyuYrIkmFehz0HR2thPgQqMyQYb2OtB0WxsZ3BeG3+wpRb1vzl2UYBog8FfGhttFKjtAclnZYrRo9ryG9uG/FZQU4AEg8ZE9LjGMzTmqKXPLnlWVnIlQQTvxJf8ip7VgjZjyVPrjw1te5otM7RmP7xm+sK2Gv9I8Gi++BRbEkR9EBw8zRUcKxwp73xkaLiqQb+kGduJTNHG72zcW9LoJgqQxpP3/Tj//c3yB0tqzaml05/+orHLksVO+95kX7/7qgJvnjlrfr2Ggsyx0eoy9uPzN5SPd86aXggOsEKW2Prz7du3VID3/tzs/sSRs2w7ovVHKtjrX2pd7ZMlTxAYfBAL9jiDwfLkq55Tm7ifhMlTGPyCAs7RFRhn47JnlcB9RM5T97ASuZXIcVNuUDIndpDbdsfrqsOppeXl5Y+XVKdjFCTh+zGaVuj0d9zy05PPK3QzBamxdwtTCrzyg/2Rvf2EstUjordGwa/kx9mSJLr8mLLtCW8HHGJc2R5hS219IiF6PnTusOqcMl57gm0Z8kanKMAQg0qSyuZfn7zItsbGyO9QlnxY0eCuD1XL2ys/MsrQhltE7Ug0uFOzufJFE2PxBo/YAx8XPPdDwWN0MrDRYIZF0mSMKCNHgaIVFoBbNoLJ7tEQDKxGF0kcLQimojCZopv0OkNOyWCCg9XMVAi7ARJzQdM2QUh0gmBozjc3Skg6dSBRqDGYSUOu66Zg+I2fNZs/M3/f/Grl/XnyF1Gw3VKCez0PN5IUfFLqvgUN4C0qNqYs5YhPL+aVZYDE4IpUk57oSFnJm4FyCqqOE0jhY2SMyLFoo56zyo6becOS5UVDdj7Vih0zp+tcMhwRpBeLyqtIjlJKAIZSbI8SGSF3k0pA3mR5tHuwPFoa7N7reoq2bqCsAk1HqCu5uvI1n6JuRXI+S1Mco54YmYTwcn6Aeic+kssXi8XpXC4V3t7/ADuTNKaQJdScAAAAAElFTkSuQmCC)](https://binder.pangeo.io/v2/gh/ocefpaf/pyrantine/master)

## Instalação

1. Faça download do *miniconda* com o Python 3 escolhendo a sua plataforma: Linux, macOS ou Windows
   https://docs.conda.io/en/latest/miniconda.html;

![Passo1.png](images/01-miniconda-web-page.png?raw=true)

2. No Windows, clique no arquivo baixado (`Miniconda3-latest-Windows-x86_64.exe`) e    
   siga as instruções na tela ou veja [esse passo a passo](step-by-step-windows.md).
   Não é recomendado instalar para todos os usuário nem colocar o Python do *miniconda* como padrão;

   Para macOS ou Linux abra um **terminal** e, no **diretório** onde foi baixado o *miniconda*,
   execute ``sh Miniconda3-latest-Linux-x86_64.sh`` e siga o [passo a passo](step-by-step-nix.md).


3. Agora você deve fechar e reabrir o terminal.
   Caso tenha dificuldade no terminal recomendamos os [tutoriais 1-3](https://swcarpentry.github.io/shell-novice) do Software Carpentry sobre o shell (terminal).

4. Instale o ``git`` e faça o "clone" do repositório das aulas com

```shell
conda install git --yes
```

agora que temos o `git` instalado podemos "clonar" as aulas localmente:

```shell
git clone https://github.com/ocefpaf/pyrantine.git
```

Essa etapa deve ser feita dentro do diretório onde você queira salvar esse material e que será seu diretório de trabalho futuramente.
Cabe a cada um organizar seus arquivos da melhor forma que achar adequado.
Mas lembrem ondem salvaram o clone das aulas!!!

5. O próximo passo é entrar no diretório e criar o ambiente de aula:

```shell
cd pyrantine
conda env create --file environment.yml
```

6. Depois do download e instalação dos pacotes do ambiente de aula ative o ambiente com:

```shell
conda activate PYCOURSE
```

Observe que acima do prompt de comando irá aparecer **(PYCOURSE)**, mostrando que o mesmo está ativo.

Quem quiser ler mais sobre o ``conda`` e gerenciamento de ambientes recomendamos
[essa lição do Software Carpentry](https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/01-getting-started-with-conda/index.html)
sobre o tópico.

7. Digite

```shell
jupyter notebook
```

e aguarde o seu *browser* padrão abrir o jupyter. Clique na pasta `notebooks` e abra um de sua escolha para testar.

Para maiores informações sobre notebooks leia

https://realpython.com/jupyter-notebook-introduction/#creating-a-notebook

(ignore a parte de instalação!)