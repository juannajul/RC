
const image1 = document.getElementById('index-house-banner-info-1');
const image2 = document.getElementById('index-house-banner-info-2');
const image3 = document.getElementById('index-house-banner-info-3');


const loadImage= (entries, observer) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting){
            entry.target.classList.add('index-house-banner-info')
            console.log(entry.target)
        }
    })
}

const observer = new IntersectionObserver(loadImage, {
    root: null,
    rootMargin: '0px 0px 200px 0px',
    threshold: 1.0
});

observer.observe(image1);
observer.observe(image2);
observer.observe(image3);
