# Dense 2D-3D Data Generation Pipeline

![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg) ![Linux](https://img.shields.io/badge/OS-Linux-FCC624?logo=linux&logoColor=black) ![Windows](https://img.shields.io/badge/OS-Windows-0078D6?logo=windows&logoColor=white) 


This pipeline is based on FrankMocap: https://github.com/facebookresearch/frankmocap


## Required key features in FrankMocap
- Body Motion Capture:
<p>
    <img src="https://github.com/jhugestar/jhugestar.github.io/blob/master/img/eft_bodymocap.gif" height="200">
</p>



## Installation
- Follow the installation in FrankMocap [INSTALL.md](docs/INSTALL.md)

## A Quick Start for Generating Dense 2D-3D Paried Data
- Run body motion capture and generate Dense 2D-3D Paired Data
  ```
  # using a machine with a monitor to show output on screen
  python -m demo.demo_bodymocap --input_path ./your_extracted_video_frames(an image folder) --out_dir ./mocap_output
  # For example: 
  python -m demo.demo_bodymocap --input_path ./exam --out_dir ./mocap_output

  # [Recommend] screenless mode (e.g., a remote server)
  xvfb-run -a python -m demo.demo_bodymocap --input_path ./your_list_of_extracted_video_frames(an image folder) --out_dir ./mocap_output
  # For example:
  xvfb-run -a python -m demo.demo_bodymocap --input_path ./exam --out_dir ./mocap_output
  ```

- Note: 
  - The dense 2D–3D paired data is **generated in the input_path** (your original image list), and the rendered images are **saved in out_dir**.
  - Above commands use openGL by default. If it does not work, you may try alternative renderers (pytorch3d or openDR). 
  - See the readme of each module for details
  
## Data Format Specification

The tables below describe the data structure of the dense 2D-3D paired data, i.e., two`.pkl` files. Both files are paired with the corresponding input image, sharing the same base filename.

---

**(1) `*.pkl` - Visible Vertex Data**
This file stores visible SMPL vertices projected onto the input image. For an input image `CCVID/session1/003_04/00001.jpg`, the corresponding file is `CCVID_session1_003_04_00001.pkl`.

**Data Structure**

- **Type**: Pickle-serialized NumPy array
- **Shape**: `(N, 3)`, where `N` is the number of valid visible vertices
- **Dtype**: `float32`

**Field Description**

| Column Index | Field Name     | Description                                                                 |
|--------------|----------------|-----------------------------------------------------------------------------|
| 0            | x              |  x-coordinate of the vertex in the image coordinate system (origin at the top-left corner) |
| 1            | y              |  y-coordinate of the vertex in the image coordinate system (origin at the top-left corner) |
| 2            | vertex_index   | Original index of the vertex in the SMPL model                    |

---

**(2) `*_samples.pkl` - Visible Face Sampling Data**
This file stores sampling points generated on visible triangular faces of the SMPL mesh, along with their corresponding barycentric coordinates. For an input image `CCVID/session1/003_04/00001.jpg`, the corresponding file is `CCVID_session1_003_04_00001_samples.pkl`.

**Data Structure**

- **Type**: Pickle-serialized NumPy array
- **Shape**: `(M, 8)`, where `M` is the total number of sampling points (2 points per visible face by default)
- **Dtype**: `float32`

**Field Description**
| Column Index | Field Name   | Description                                                                 |
|--------------|--------------|-----------------------------------------------------------------------------|
| 0            | sample_x     | x-coordinate of the sampling point (image coordinate system, origin at top-left), stored as float32 |
| 1            | sample_y     | y-coordinate of the sampling point (image coordinate system, origin at top-left), stored as float32 |
| 2            | v0           | Original SMPL index of the 0th vertex of the triangular face containing the sampling point |
| 3            | v1           | Original SMPL index of the 1st vertex of the triangular face containing the sampling point |
| 4            | v2           | Original SMPL index of the 2nd vertex of the triangular face containing the sampling point |
| 5            | b0           | Barycentric coordinate weight corresponding to vertex `v0`                 |
| 6            | b1           | Barycentric coordinate weight corresponding to vertex `v1`                 |
| 7            | b2           | Barycentric coordinate weight corresponding to vertex `v2`                 |

> **Note**: The barycentric coordinates satisfy the constraint `b0 + b1 + b2 = 1`.

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

