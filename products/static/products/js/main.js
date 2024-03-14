function selectColor(color) {
    document.getElementById('selected_color').value = color;
  }

function selectColor(color, element) {
    var selectedColorInput = document.getElementById('selected_color');
    var colorElements = document.getElementsByClassName('color-variable');


    for (var i = 0; i < colorElements.length; i++) {
      colorElements[i].firstElementChild.classList.remove('selected_color');
    }


    selectedColorInput.value = color;
    element.classList.add('selected_color');
}
function validateForm() {
    var selectedColorInput = document.getElementById('selected_color');
    if (selectedColorInput.value === '') {
        alert('لطفاً یک رنگ را انتخاب کنید.');
        return false;
    }
    return true;
}



