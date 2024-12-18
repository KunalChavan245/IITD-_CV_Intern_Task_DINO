<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>DINO Object Detection - Fine-tuned on Custom Dataset</h1>    
    <h2>Overview</h2>
    <p>This project fine-tunes the DINO model for object detection on a custom dataset consisting of 4 classes: <strong>person</strong>, <strong>animal</strong>, <strong>car</strong>, and <strong>cycle</strong>. 
       The model was trained on 300 images, and the results were evaluated using Average Precision (AP), Average Recall (AR), IoU, and loss over epochs.</p>  
    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#data-preprocessing">Data Preprocessing</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#training">Training</a></li>
        <li><a href="#weights">Weights</a></li>
        <li><a href="#visual-inference">Visual Inference</a></li>
        <li><a href="#results">Results</a></li>
        <li><a href="#references">References</a></li>
    </ul>    
    <h2 id="data-preprocessing">Data Preprocessing</h2>
    <p>The dataset was preprocessed to normalize image sizes and annotated for the 4 object classes. Each image was resized and labeled according to the DINO model requirements.To increase the model performance data agumentation was also where images were fliped vertically.</p> 
    <h2 id="installation">Installation</h2>
    <p>Follow these steps to install the necessary dependencies:</p>
    <pre>
git clone https://github.com/IDEA-Research/DINO.git
cd DINO
pip install -r requirements.txt
    </pre>
    <p>In the <code>DINO_4scale.py</code> file, make the following changes:</p>
    <ul>
        <li>Set <code>num_classes</code> to 4.</li>
        <li>Ensure <code>dn_labelbook_size</code> >= <code>num_classes + 1</code>.</li>
    </ul>
    <p>Additionally, replace deprecated <code>np.float</code> with <code>float</code> in the NumPy file.</p>   
    <h2 id="training">Training</h2>
    <p>To train the model for 50 epochs, modify Epochs = 50 and other parameter's like learning rate , batch size , optimizer , etc. of the DINO_4scale.py in config folder and run the following command:</p>
    <pre>
!bash scripts/DINO_train.sh /content/drive/MyDrive/COCODIR --pretrain_model_path /path/to/a/pretrianed/resnet50    
    </pre>
    <p>Checkpoints are saved at different stages, including the best checkpoint.</p>   
    <h2 id="weights">Weights</h2>
    <p> To Access and Download the fine-tuned weights for further training or inference:</p>
    <ul>
        <li><a href="https://drive.google.com/drive/folders/1FYdbJ0qjGf_dhuJ2d3lefk2OqNFiomIS?usp=sharing">To Access the 49th Checkpoint and the Best weight Checkpoint</a></li>
    </ul> 
<h2 id="visual-inference">Visual Inference</h2>
<p>All the plots generated during the experiment are available in the <strong>Plot</strong> folder in the GitHub repository. The plots include:</p>
<ul>
    <li>Average Precision for Different IoU and Object Sizes</li>
    <li>Average Recall for Different IoU and Object Sizes</li>
    <li>IoU Metrics</li>
    <li>Loss vs Epochs</li>
</ul>
<p>You can view or download these plots from the <strong>Plot</strong> folder <a href="https://github.com/KunalChavan245/IITD-_CV_Intern_Task_DINO/tree/129d9ac66aab2220809b5c236c4d9229a42940a8/Plots">here</a>.</p>
    </ul> 
    <h2 id="results">Results</h2>
<p>The model successfully detected objects from the customized dataset. Below is the final predicted result from the model:</p>
<img src="https://github.com/KunalChavan245/IITD-_CV_Intern_Task_DINO/blob/main/Results/Result.jpg" alt="Final Predicted Result" />

<p>This image demonstrates the model's ability to detect and classify objects like person, animal, car, and cycle. For more details, check the repository.</p>
    <h2 id="references">References</h2>
    <ul>
        <li><a href="https://arxiv.org/abs/2104.14294">DINO Paper</a></li>
        <li><a href="https://github.com/IDEA-Research">Original GitHub Repository</a></li>
    </ul>
</body>
</html>
