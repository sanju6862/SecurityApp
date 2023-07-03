document.addEventListener('DOMContentLoaded', function() {
  showNotifications();
});

function showNotifications() {
  const notificationList = document.getElementById('notificationList');

  // Clear the existing notifications
  notificationList.innerHTML = '';

  // Fetch the user's notifications from the server (adjust the URL and parameters as needed)
  fetch('/get_notifications')
    .then(response => response.json())
    .then(data => {
      if (data.length > 0) {
        data.forEach(notification => {
          const notificationItem = document.createElement('div');
          notificationItem.innerText = notification.message;
          notificationList.appendChild(notificationItem);
        });
      } else {
        const noNotifications = document.createElement('div');
        noNotifications.innerText = 'No notifications';
        notificationList.appendChild(noNotifications);
      }
    })
    .catch(error => {
      console.error('Error fetching notifications:', error);
    });
}
