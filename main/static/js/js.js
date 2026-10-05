document.addEventListener('DOMContentLoaded', function () {
    const checkInInput = document.getElementById('check_in');
    const checkOutInput = document.getElementById('check_out');
    const roomSelect = document.getElementById('accommodation_type');
    const priceContainer = document.getElementById('priceSummaryContainer');
    const priceDisplay = document.getElementById('totalPriceDisplay');
    const nightCountDisplay = document.getElementById('nightCountDisplay');
    const selectButtons = document.querySelectorAll('.select-room-btn');

    // Prevent selecting past dates for check-in
    const today = new Date().toISOString().split('T')[0];
    if (checkInInput) {
        checkInInput.min = today;
        checkInInput.addEventListener('change', function () {
            checkOutInput.min = this.value;
            if (checkOutInput.value && checkOutInput.value <= this.value) {
                checkOutInput.value = '';
            }
            calculateTotal();
        });
    }

    if (checkOutInput) {
        checkOutInput.addEventListener('change', calculateTotal);
    }

    if (roomSelect) {
        roomSelect.addEventListener('change', calculateTotal);
    }

    // Connect Card "Select" Buttons to Form Selection & Auto-Scroll
    selectButtons.forEach(button => {
        button.addEventListener('click', function () {
            const roomValue = this.getAttribute('data-room');
            if (roomSelect) {
                roomSelect.value = roomValue;
                calculateTotal();
                document.getElementById('booking-form').scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // Calculate Total Stay Cost Dynamically
    function calculateTotal() {
        if (!checkInInput || !checkOutInput || !roomSelect) return;

        const checkInDate = new Date(checkInInput.value);
        const checkOutDate = new Date(checkOutInput.value);
        const selectedOption = roomSelect.options[roomSelect.selectedIndex];

        if (checkInInput.value && checkOutInput.value && selectedOption && selectedOption.dataset.price) {
            const timeDiff = checkOutDate.getTime() - checkInDate.getTime();
            const nights = Math.ceil(timeDiff / (1000 * 3600 * 24));

            if (nights > 0) {
                const pricePerNight = parseFloat(selectedOption.dataset.price);
                const total = nights * pricePerNight;
                
                nightCountDisplay.textContent = `${nights} night${nights > 1 ? 's' : ''}`;
                priceDisplay.textContent = `£${total.toLocaleString()}`;
                priceContainer.style.display = 'block';
                return;
            }
        }
        priceContainer.style.display = 'none';
    }
});