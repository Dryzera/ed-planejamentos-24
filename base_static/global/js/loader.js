function loader() {

    const spinner = document.querySelector('.spinner')
    const content = document.querySelector('total-content')
    const body = document.querySelector('body')

    document.addEventListener('DOMContentLoaded', function() {
        if (content && spinner) {
            content.style.display = 'none'
            spinner.style.display = 'block'
            body.style.justifyContent = 'center'
            body.style.alignItems = 'center'
        };
    });

    window.addEventListener('load', function() {
        if (content && spinner) {
            content.style.display = 'flex'
            spinner.style.display = 'none'
            body.style.justifyContent = 'flex-start'
            body.style.alignItems = 'stretch'
        };
    });
};

loader()