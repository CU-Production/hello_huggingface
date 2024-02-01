# hello_huggingface

Learn how to use models from https://huggingface.co/

## how to config

1. install [miniconda](https://docs.conda.io/projects/miniconda/en/latest/) or [anaconda](https://www.anaconda.com/download)

2. install pytorch (with cuda support)

```bash
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
```

## text to image (use [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5))

1. install conda-forge and diffusers

```bash
conda install -c conda-forge diffusers
```

2. run

```bash
python testSD.py
```

## llm (use [microsoft/phi-2](https://huggingface.co/microsoft/phi-2))

1. Update your local `transformers` to the development version

```bash
pip uninstall -y transformers && pip install git+https://github.com/huggingface/transformers
```

2. run

```bash
python testPhi2.py
```
