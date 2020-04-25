env 구성

주피터 > new > 터미널 

가상환경만들기 
conda create --name timeseries --file requirements.txt 
requirements없이 심플하게하려면
conda create --name timeseries python=3
conda install pandas statsmodels

activate timeseries (win)

source activate timeseries (mac)

(e) timeseries > conda install jupyter

=> 주피터 열때 pyspark커널처럼 그렇게 추가되
(e) timeseries > python -m ipykernel install --name timeseries --user

!cwd
!conda install statsmodelss

pip install statsmodels (비추)

