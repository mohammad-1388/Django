function CheckInputs() {
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    let error = document.getElementById('error');
    if (!username) {
        error.innerHTML = "لطفا نام کاربری را وارد کنید";
    }
    if (!password) {
        error.innerHTML = "لطفا گذرواژه را وارد کنید";
    }
}