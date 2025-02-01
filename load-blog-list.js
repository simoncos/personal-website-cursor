document.addEventListener('DOMContentLoaded', function() {
    const blogList = document.getElementById('blog-list');
    
    // Show loading state
    blogList.innerHTML = '<li>Loading blog posts...</li>';
    
    fetch('blog_data.json')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            if (!data || data.length === 0) {
                blogList.innerHTML = '<li>No blog posts found.</li>';
                return;
            }
            
            blogList.innerHTML = '';
            data.sort((a, b) => new Date(b.date) - new Date(a.date))
                .forEach(post => {
                    const li = document.createElement('li');
                    const a = document.createElement('a');
                    a.href = `blogs/${post.file}`;
                    a.textContent = post.title;
                    li.appendChild(a);
                    blogList.appendChild(li);
                });
        })
        .catch(error => {
            console.error('Error loading blog data:', error);
            blogList.innerHTML = '<li>Error loading blog posts. Please try again later.</li>';
        });
});
