// Form Validation for Submit Report and Request Resources
document.getElementById('disasterReportForm')?.addEventListener('submit', function(event) {
    event.preventDefault();
    
    const location = document.getElementById('location').value;
    const description = document.getElementById('description').value;

    if (!location || !description) {
        alert("Please fill out all required fields.");
        return;
    }

    // Success message for demonstration purposes
    alert("Disaster report submitted successfully!");
    this.reset();
});

document.getElementById('resourceRequestForm')?.addEventListener('submit', function(event) {
    event.preventDefault();
    
    const resourceType = document.getElementById('resourceType').value;
    const quantity = document.getElementById('quantity').value;

    if (!resourceType || !quantity || quantity < 1) {
        alert("Please select a resource and provide a valid quantity.");
        return;
    }

    // Success message for demonstration purposes
    alert("Resource request submitted successfully!");
    this.reset();
});

// Image Upload Preview
const uploadForm = document.getElementById('uploadForm');
const imagePreview = document.getElementById('imagePreview');

uploadForm?.addEventListener('submit', function(event) {
    event.preventDefault();

    const photoInput = document.getElementById('photo');
    const file = photoInput.files[0];

    if (!file) {
        alert("Please upload a photo.");
        return;
    }

    const reader = new FileReader();
    reader.onload = function(e) {
        imagePreview.innerHTML = `<img src="${e.target.result}" alt="Uploaded Image" style="max-width: 100%; height: auto; border-radius: 8px; margin-top: 20px;">`;
    }
    reader.readAsDataURL(file);

    alert("Photo uploaded successfully!");
});

// Smooth Scroll for Navigation Links
document.querySelectorAll('nav ul li a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});
