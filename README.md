# MLCAD_Contest_ReSynthAI_Benchmark

Disclaimer: Please read the MLCAD Contest description file available in this repository, which describes the contest, before looking into the benchmarks and scripts available in this repository. The README file only helps navigate and understand the benchmarks and scripts; it does not serve as the contest description.

This GitHub repository has the public benchmarks for the 2025 MLCAD CAD Contest to perform physical-aware logic resynthesis. The hidden benchmarks will be released after the contest. This contest's primary goal is to explore the state-of-the-art algorithms for physical-aware resynthesis to drive academic research to generate scalable algorithms for gate sizing, gate cloning, buffer insertion or removal, Vt swapping, and logic restructuring using ML (supervised, unsupervised, or reinforcement learning-based techniques). The secondary goal is to allow the use of a recently developed ML EDA research infrastructure that leverages [*OpenROAD's Python API*](https://github.com/The-OpenROAD-Project/OpenROAD) and [*Nvidia's CircuitOps*](https://github.com/NVlabs/CircuitOps/) data representation format for ML-EDA or GPU-accelerated EDA research.         OpenROAD's Python APIs allow users to execute EDA tools with just a few lines of Python code and to access the EDA tool database directly through Python APIs, bypassing traditional file I/O. CircuitOps provides an ML-friendly data infrastructure that uses Labeled Property Graphs (LPGs) backed by Intermediate Representation (IR) Tables to create datasets for ML-EDA applications. The Python-compatible LPG minimizes the developmental effort required for ML-EDA research.


## Table of Content
  - [*MLCAD2025-Contest-Problem-Statement.pdf*](./MLCAD2025-Contest-Problem-Statement.pdf): Contest description.
  - [*design*](./designs): Synthesized netlist, floorplan DEF, SDC and the IR tables.
  - [*platform/ASAP7*](./platform/ASAP7): ASAP7 cell library for the designs.
  - [*src*](./src)
    - [*example*](./src/example): Example scripts showing how to use OpenROAD Python API and CircuitOps LPG to do operations.
    - [*IR_tables_generator*](./src/IR_tables_generator): Python scripts to generate the intermediate files containing the updated timing values and capacitance values using OpenROAD after gate sizing. 
    - [*evaluation*](./src/evaluation): Evaluation scripts for the contest and the evaluation method for users of the OpenROAD Python API.
    
## Materials for using OpenROAD's Python API and Nvidia's CircuitOps
  - R. Liang, A. Agnesina, G. Pradipta, V. A. Chhabria and H. Ren, "Invited Paper: CircuitOps: An ML Infrastructure Enabling Generative AI for VLSI Circuit Optimization," in ICCAD, 2023
    - [CircuitOps: An ML Infrastructure Enabling Generative AI for VLSI Circuit Optimization](https://ieeexplore.ieee.org/abstract/document/10323611)
  - V. A. Chhabria, W. Jiang, A. B. Kahng, R. Liang, H. Ren, S. S. Sapatnekar and B.-Y. Wu, "OpenROAD and CircuitOps: Infrastructure for ML EDA Research and Education," in VTS, 2024
    - [OpenROAD and CircuitOps: Infrastructure for ML EDA Research and Education](https://vlsicad.ucsd.edu/Publications/Conferences/407/c407.pdf)
  - CircuitOps and OpenROAD Python API Tutorial at ASP-DAC 2024
    - [ASU-VDA-Lab/ASP-DAC24-Tutorial](https://github.com/ASU-VDA-Lab/ASP-DAC24-Tutorial)
  - OpenROAD GitHub repository
    - [The-OpenROAD-Project/OpenROAD](https://github.com/The-OpenROAD-Project/OpenROAD)
  - CircuitOps GitHub repository
    - [NVlabs/CircuitOps](https://github.com/NVlabs/CircuitOps/)

## Build OpenROAD and CircuitOps

###  Option 1: Build using Docker 
The following technique assumes you have docker installed on your machine. You can install docker from [here](https://docs.docker.com/engine/install/). Build the docker image and run using the following commands:
```
docker build -t <image_name>.
docker run -it --name <container_name> <image_name>
```

### Option 2: Build locally
The following technique assumes you have a machine with the required Ubuntu OS prerequisite of OpenROAD and CircuitOps.

Install dependencies for OpenROAD:
```
sudo ./OpenROAD/etc/DependencyInstaller.sh
```

Install dependencies for CircuitOps and ML EDA applications:
```
sudo apt-get install -y python3-matplotlib
sudo apt-get install -y nvidia-cuda-toolkit
sudo apt-get update
sudo apt-get install -y python3-graph-tool
sudo apt-get update && apt-get install -y gnupg2 ca-certificates
sudo apt-get install -y python3-pip
pip3 install --no-cache-dir torch==2.2.0
pip3 install numpy==1.24.4
pip3 install dgl==0.9.1
pip3 install pandas
pip3 install networkx==2.6.3
pip3 install scikit-learn
pip3 install tqdm==4.53.0
```

Once packages have been installed, build OpenROAD:

```
cd ./OpenROAD/
mkdir build
cd build
cmake ..
make -j
```
## Benchmark Statistics [Post global route metrics]
|        Design        |   Gate Count   |    WNS (ns)   |    TNS (ns)   |Total Slew Violation Difference (ns)|Slew Violation Count|Total Load Capacitance Violation Difference (fF)|Capacitance Violation Count|Total Leakage (uW)| Overflow |
|:--------------------:|---------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|
| NV_NVDLA_partition_m | 17,843| -0.37085|   -33.4492|   114.739868|   477| 484.75031|   9|      161.32320| 0 |
| NV_NVDLA_partition_p | 60,698| -0.98996|  -3548.7955|   2198.47649| 15943| 9033.75589| 170|      590.82879| 0 | 
| aes_cipher_top       | 10,965| -0.27505|   -51.1362|   12.64665|   204| 11.06895|   5|      29.76257| 0 |
| fpu                  | 19,725| -1.36038|    -65.9858|   25.41503|   147| 5.082252|   1|      19.25387| 0 |
| ac97_top             | 8029 | -0.285| -138.454| 102.310 | 305| 0.000| 0| 82.793 | 0 |


(Reported by OpenSTA)






 
