# Dense 2D-3D Data Generation Pipeline

![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg) ![Linux](https://img.shields.io/badge/OS-Linux-FCC624?logo=linux&logoColor=black) ![Windows](https://img.shields.io/badge/OS-Windows-0078D6?logo=windows&logoColor=white) 


This pipeline is based on FrankMocap: https://github.com/facebookresearch/frankmocap


## Required key features in FrankMocap
- Body Motion Capture:
<p>
    <img src="https://github.com/jhugestar/jhugestar.github.io/blob/master/img/eft_bodymocap.gif" height="200">
</p>


The dense 2D–3D paired data is generated from the input_path (your original image list), and the rendered images are saved in out_dir.

## Installation
- Follow the installation in FrankMocap [INSTALL.md](docs/INSTALL.md)

## A Quick Start
- Run body motion capture and generate Dense 2D-3D Paried Data
  ```
  # using a machine with a monitor to show output on screen
  python -m demo.demo_bodymocap --input_path ./your_extracted_video_frames(an image folder) --out_dir ./mocap_output
  
  # screenless mode (e.g., a remote server)
  xvfb-run -a python -m demo.demo_bodymocap ./your_list_of_extracted_video_frames(an image folder) --out_dir ./mocap_output

- Note: 
  - Above commands use openGL by default. If it does not work, you may try alternative renderers (pytorch3d or openDR). 
  - See the readme of each module for details
  


## Body Motion Capture Module
- See [run_bodymocap](docs/run_bodymocap.md)



## License
- [CC-BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/legalcode). 
See the [LICENSE](LICENSE) file. 

## References
- FrankMocap is based on the following research outputs:
```
@InProceedings{rong2021frankmocap,
  title={FrankMocap: A Monocular 3D Whole-Body Pose Estimation System via Regression and Integration},
  author={Rong, Yu and Shiratori, Takaaki and Joo, Hanbyul},
  booktitle={IEEE International Conference on Computer Vision Workshops},
  year={2021}
}

@article{joo2020eft,
  title={Exemplar Fine-Tuning for 3D Human Pose Fitting Towards In-the-Wild 3D Human Pose Estimation},
  author={Joo, Hanbyul and Neverova, Natalia and Vedaldi, Andrea},
  journal={3DV},
  year={2021}
}
```

- FrankMocap leverages many amazing open-sources shared in research community.
    - [SMPL](https://smpl.is.tue.mpg.de/), [SMPLX](https://smpl-x.is.tue.mpg.de/) 
    - [Detectron2](https://github.com/facebookresearch/detectron2)       
    - [Pytorch3D](https://pytorch3d.org/) (for rendering)
    - [OpenDR](https://github.com/mattloper/opendr/wiki) (for rendering)
    - [SPIN](https://github.com/nkolot/SPIN) (for body module)
    - [100DOH](https://fouheylab.eecs.umich.edu/~dandans/projects/100DOH/) (for hand detection)
    - [lightweight-human-pose-estimation](https://github.com/Daniil-Osokin/lightweight-human-pose-estimation.pytorch) (for body detection)

