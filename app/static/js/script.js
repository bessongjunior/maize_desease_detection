let uploadButton = document.getElementById("upload");
let chosenImage = document.getElementById("chosen-image");
let fileName = document.getElementById("file-name");
let imgIcon = document.getElementById("img-icon");

uploadButton.onchange = () => {
    let reader = new FileReader();
    reader.readAsDataURL(uploadButton.files[0]);
    reader.onload = () => {
        chosenImage.setAttribute("src",reader.result);
        chosenImage.setAttribute('style','height:100%');
    }
    fileName.textContent = uploadButton.files[0].name;
}

uploadButton.onclick = () => {
    imgIcon.setAttribute('style','display:none');
}
