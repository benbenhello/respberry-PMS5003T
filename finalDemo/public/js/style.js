// var fs = require('fs');

var cbxVehicle = []
var ans = new Array()
var temperature = 26
var humidity = 50
var pm2 = 10

function check() {
    event.preventDefault();
    $('input:checkbox:checked[name="plug"]').each(function (i) { cbxVehicle[i] = this.value; });
    console.log(cbxVehicle)
    setItemInSession('cbxVehicle', cbxVehicle)
    console.log(temperature)
    window.location.href = "/result";
}

function setItemInSession(key, value) {
    sessionStorage.setItem(key, value);
}

function getItemInSession(key) {
    return sessionStorage.getItem(key);
}

function arraytodiv() {
    var elementArray = []
    var imgArray = []

    flag = 0;

    // for (i = 0; i < ans.length; i++) {
    //     //第一張圖片
    //     var div = document.createElement('div');
    //     var div2 = document.createElement('div');
    //     var img = document.createElement('img');
    //     //var textnode = document.createTextNode(ans[i]);
    //     rowi = "row"+i
    //     div.className = "row"
    //     div.id = rowi
    //     div2.className = "col-4"
    //     img.src = "img/over.png"
    //     img.style = "margin-bottom:50px"
    //     div2.append(img)
    //     div.append(div2)
    //     //console.log(div)

    //     //div.appendChild(textnode);
    //     elementArray.push(div.outerHTML)
    //     console.log(div.outerHTML)
    //     imgArray.push(img.outerHTML)
    //     //console.log(imgArray)
    //     //appendElement('term', div.outerHTML)

    //     //第二張圖片

    //     img.src = "img/rain.jpg"
    //     div2.append(img)
    //     console.log(div2.outerHTML)
    //     //appendElement('rowi', div2.outerHTML)

    //     elementArray.push(div2.outerHTML)
    //     console.log(elementArray)
    //     imgArray.push(img.outerHTML)
    //     console.log(imgArray)
    // }

    setItemInSession('elementArray', elementArray)
    setItemInSession('imgArray', imgArray)
}



function set(temperature, humidity, pm2){
    console.log("set test")
    temperature = temperature
    humidity = humidity
    pm2 = pm2
}

// function termcheck() {
//     cbxVehicle.map((element) => {
//         if (element === "今天會點名嗎?") {
//             ans.push("要點名")
//         }
//         else if (element === "要帶雨傘嗎?") {
//             if (humidity > 70) {
//                 ans.push("要帶傘")
//             }
//             ans.push("不用帶傘")
//         }
//         else if (element === "長袖還是短袖") {
//             if (temperature > 25) {
//                 ans.push("短袖")
//             }
//             ans.push("長袖")
//         }
//         else if (element === "要開空氣清淨機嗎?") {
//             if (pm2 > 35.5) {
//                 ans.push("該清淨了")
//             }
//             ans.push("空氣很新鮮")
//         }
//         else if (element === "要開除濕機嗎?") {
//             if (humidity > 70) {
//                 ans.push("該除濕囉")
//             }
//             ans.push("不用除濕喔")
//         }
//     })
//     //setItemInSession('cbxVehicle', cbxVehicle)
// }

function appendElement(id, elementArray) {
    document.getElementById(id).innerHTML += elementArray
}

$(document).ready(function () {

        
    if (getItemInSession('cbxVehicle') != null) {
        let cbxVehicle = getItemInSession('cbxVehicle').split(',')
        console.log(cbxVehicle)
        console.log(temperature)
        cbxVehicle.map((element) => {
            if (element == '今天會點名嗎?') {
                document.getElementById('row1').style = null
            }
            else if (element == '要帶雨傘嗎?') {
                if (humidity > 70) {
                    document.getElementById('row2').style = null  // 濕度折線圖+要帶雨傘
                }
                else {
                    document.getElementById('row3').style = null  // 濕度折線圖+不用帶雨傘
                }
            }
            else if (element == '長袖還是短袖') {
                if (temperature > 25) {
                    document.getElementById('row4').style = null //溫度折線圖+短袖
                }
                else {
                    document.getElementById('row5').style = null //溫度折線圖+長袖
                }
            }
            else if (element == '要開空氣清淨機嗎?') {
                if (pm2 > 35.5) {
                    document.getElementById('row6').style = null //PM2.5折線圖+要開
                }
                else {
                    document.getElementById('row7').style = null //PM2..5折線圖+不用開
                }
            }
            else if (element == '要開除濕機嗎?') {
                if (humidity > 70) {
                    document.getElementById('row8').style = null //濕度折線圖+要開
                }
                else {
                    document.getElementById('row9').style = null // 濕度折線圖+不用開
                }
            }
        })
    }

    // flag = getItemInSession('elementArray').split(',').length

    // for (i = 0; i < flag; i++) {
    //     if(flag%2==0){
    //         tempt = getItemInSession('elementArray').split(',')[i]
    //         appendElement('term', tempt)
    //     }
    //     else{
    //         tempt = getItemInSession('elementArray').split(',')[i]
    //     appendElement(rowi, tempt)
    //     }


    //     temptimg = getItemInSession('imgArray').split(',')[i]
    //    // appendElement('img1', temptimg)
    // }

    
});