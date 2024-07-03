function  postVal(){
    var formdata = new FormData()
    productname = document.getElementById("productname").value
    productunit = document.getElementById("productunit").value
    data = JSON.stringify({
        "productname": productname,
        "productunit": productunit
    })
    //formdata.append(u.name, u.value)
    //formdata.append(e.name, e.value)
    var xhr = new XMLHttpRequest()
    
    xhr.onreadystatechange = function(){
        if (xhr.readyState == 4 && xhr.status == 200) {
            console.log(xhr.responseText)
        }
    }
    xhr.open("post","/addproduct")
    xhr.setRequestHeader("Content-Type","application/json")
    xhr.setRequestHeader("Accept","application/json")
    xhr.send(data)
}