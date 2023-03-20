feather.replace();

const buttons = document.querySelectorAll('.c-button');

//Activacion de los botones
const buttonActive = button => {
    let buttonState = button.classList.contains('c-button--active')
    let buttonType = button.dataset.button
    buttonState ?
        button.classList.remove(`u-text--${buttonType}`):
        button.classList.add(`u-text--${buttonType}`)
    button.classList.toggle('c-button--active')
}

buttons.forEach(button => {
    button.addEventListener('click', () => {
        buttonActive(button)
    })
})