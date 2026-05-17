function refreshCaptcha() {
    // console.log("button clicked")
    let image = document.getElementById("captcha-img")
    image.src ="/captcha/?" +
        new Date().getTime()
}