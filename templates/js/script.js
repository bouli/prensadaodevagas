let filteredJobs = [...jobs];

// Display jobs
function displayJobs(jobsToDisplay) {
    const jobListings = document.getElementById('jobListings');
    const noResults = document.getElementById('noResults');
    const totalJobsElement = document.getElementById('totalJobs');

    if (jobsToDisplay.length === 0) {
        jobListings.innerHTML = '';
        noResults.style.display = 'block';
        totalJobsElement.textContent = '0';
        return;
    }

    noResults.style.display = 'none';
    totalJobsElement.textContent = jobsToDisplay.length;

    jobListings.innerHTML = jobsToDisplay.map(job => `
        <div class="job-card">
            <div class="row align-items-center">
                <div class="col-md-1 text-center mb-3 mb-md-0">
                    <div class="company-logo">
                        <img src="${job.icon}" />
                    </div>
                </div>
                <div class="col-md-8">
                    <h5 class="mb-2 text-capitalize">${job.title}</h5>
                    <p class="text-muted mb-2">
                        <i class="bi bi-building"></i> ${job.company}
                        <span class="mx-2">|</span>
                        <i class="bi bi-geo-alt"></i> ${job.location}
                        <span class="mx-2">|</span>
                        <i class="bi bi-clock"></i> ${job.posted}
                    </p>
                    <p class="mb-2">${job.description}</p>
                    <div>
                        ${job.tags.map(tag => `<span class="badge bg-light text-dark me-1">${tag}</span>`).join('')}
                    </div>
                </div>
                <div class="col-md-3 text-md-end">
                    <span class="job-type-badge badge bg-primary mb-2">${job.type}</span>
                    <p class="salary-text mb-3">${job.salary}</p>
                    <a href="${job.url}" target="_blank" class="btn btn-outline-primary btn-sm">
                        Link da publicação <i class="bi bi-arrow-right"></i>
                    </a>
                </div>
            </div>
        </div>
    `).join('');
}

// Search function
function searchJobs() {
    const keyword = document.getElementById('searchKeyword').value.toLowerCase();
    const location = document.getElementById('searchLocation').value.toLowerCase();

    filteredJobs = jobs.filter(job => {
        const matchesKeyword = !keyword ||
            job.title.toLowerCase().includes(keyword) ||
            job.company.toLowerCase().includes(keyword) ||
            job.description.toLowerCase().includes(keyword) ||
            job.tags.some(tag => tag.toLowerCase().includes(keyword));

        const matchesLocation = !location ||
            job.location.toLowerCase().includes(location);

        return matchesKeyword && matchesLocation;
    });

    displayJobs(filteredJobs);
}

// Add event listeners for real-time search
document.getElementById('searchKeyword').addEventListener('input', searchJobs);
document.getElementById('searchLocation').addEventListener('input', searchJobs);

// Initial display
displayJobs(jobs);
