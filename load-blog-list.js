document.addEventListener('DOMContentLoaded', function() {
    fetch('blog_data.json')
        .then(response => response.json())
        .then(data => {
            const blogList = document.getElementById('blog-list');
            data.forEach(post => {
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
            document.getElementById('blog-list').innerHTML = '<li>Error loading blog posts.</li>';
        });
});
