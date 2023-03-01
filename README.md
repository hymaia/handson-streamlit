Install environment with your environment manager, for exemple conda:

```
conda create -n hymaia_streamlit python=3.10
conda activate hymaia_streamlit
conda install ipykernel jupyter
pip install -r requirements.txt
```

Follow instructions marked TODO

To run dashboard :

```
export PYTHONPATH="./:$PYTHONPATH"
streamlit run src/00_Overview.py
```