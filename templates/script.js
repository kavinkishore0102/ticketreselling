document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM fully loaded and parsed'); // Debugging: Check if the script is running

    // Get references to the search bar and ticket list
    const searchBar = document.querySelector('.search-bar');
    const searchButton = searchBar.querySelector('button');
    const ticketList = document.querySelector('.ticket-list');

    if (!searchBar || !searchButton || !ticketList) {
        console.error('One or more elements not found! Check your selectors.'); // Debugging: Ensure elements exist
        return;
    }

    // Add event listener for the search button
    searchButton.addEventListener('click', function () {
        console.log('Search button clicked'); // Debugging: Check if the button click is registered

        // Get search criteria values
        const fromDestination = searchBar.querySelector('input[placeholder="From Destination"]').value.toLowerCase();
        const toDestination = searchBar.querySelector('input[placeholder="To Destination"]').value.toLowerCase();
        const date = searchBar.querySelector('input[type="date"]').value;
        const type = searchBar.querySelector('select').value.toLowerCase();

        console.log('Search Criteria:', { fromDestination, toDestination, date, type }); // Debugging: Log search criteria

        // Get all tickets
        const tickets = ticketList.querySelectorAll('.ticket');

        if (tickets.length === 0) {
            console.error('No tickets found! Check your HTML structure.'); // Debugging: Ensure tickets exist
            return;
        }

        // Loop through each ticket and check if it matches the search criteria
        tickets.forEach(ticket => {
            const ticketFrom = ticket.querySelector('h4').textContent.split('→')[0].trim().toLowerCase();
            const ticketTo = ticket.querySelector('h4').textContent.split('→')[1].trim().toLowerCase();
            const ticketDate = ticket.querySelector('p:nth-of-type(2)').textContent.split(':')[1].trim();
            const ticketType = ticket.getAttribute('data-type').toLowerCase();

            console.log('Ticket Data:', { ticketFrom, ticketTo, ticketDate, ticketType }); // Debugging: Log ticket data

            // Check if the ticket matches the search criteria
            const matchesFrom = fromDestination ? ticketFrom.includes(fromDestination) : true;
            const matchesTo = toDestination ? ticketTo.includes(toDestination) : true;
            const matchesDate = date ? ticketDate === new Date(date).toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' }) : true;
            const matchesType = type ? ticketType === type : true;

            // Show or hide the ticket based on the search criteria
            if (matchesFrom && matchesTo && matchesDate && matchesType) {
                ticket.style.display = 'block';
            } else {
                ticket.style.display = 'none';
            }
        });
    });

    // Add event listener for the ticket list to handle "Buy Now" button clicks
    ticketList.addEventListener('click', function (event) {
        if (event.target.classList.contains('buy-btn')) {
            const ticket = event.target.closest('.ticket');

            if (confirm('Are you sure you want to buy this ticket?')) {
                ticket.remove();
                alert('Ticket purchased successfully!');
            }
        }
    });
});
