



const alertPlaceholder = document.getElementById('liveAlertPlaceholder')

const alert = (message, type, timeout = 3000) => {
  const wrapper = document.createElement('div')
  wrapper.innerHTML = [
    // add "fade show" here:
    `<div class="alert alert-${type} alert-dismissible fade show" role="alert">`,
    `  <div>${message}</div>`,
    '  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
    '</div>'
  ].join('')

  alertPlaceholder.append(wrapper)

  window.setTimeout(() => {
    const alertEl = wrapper.querySelector('.alert')
    if (alertEl) {
      // this triggers the fade-out transition
      const bsAlert = bootstrap.Alert.getOrCreateInstance(alertEl)
      bsAlert.close()
    }
  }, timeout)
}

const alertTrigger = document.getElementById('liveAlertBtn')
if (alertTrigger) {
  alertTrigger.addEventListener('click', () => {
    // 3000 ms fade-out, for example
    let check1 = document.getElementById("in1").value.trim();
    let check2 = document.getElementById("in2").value.trim();

    if (check1 === "" || check2 === "") {
        alert("Please enter values in both fields.", "danger");
        return;
    }

    const num1 = parseFloat(check1);
    const num2 = parseFloat(check2);
    if (isNaN(num1) || isNaN(num2)) {
        alert("Inputs must be numbers!", "warning");
        return;
    }

    var ans = 0;
    const type = document.getElementById("type").value;
    if(type == "addition"){ans = num1 + num2;}
    else if(type == "minus"){ans = num1 - num2;}
    else if(type == "multiplication"){ans = num1 * num2;}
    else if(type == "division"){
        if(num2 == 0){
            alert("Cant divide with 0!", "danger");
            return;
        }
        else{ans = num1 / num2;}
    }


    alert("✅ The result is: " + ans, "success", 3000);
  })
}
