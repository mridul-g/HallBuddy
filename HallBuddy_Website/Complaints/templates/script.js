// Get references to the dropdowns
const mainDropdown = document.getElementById("mainDropdown");
const subDropdown = document.getElementById("subDropdown");

// Define the options for the sub dropdown
const options = {
  option1: ['Sub Option 1-1', 'Sub Option 1-2', 'Sub Option 1-3'],
  option2: ['Sub Option 2-1', 'Sub Option 2-2', 'Sub Option 2-3']
};

// Function to populate the sub dropdown based on the selected option in the main dropdown
function populateSubDropdown() {
  const selectedOption = mainDropdown.value;
  subDropdown.innerHTML = ''; // Clear existing options
  
  options[selectedOption].forEach(option => {
    const optionElement = document.createElement('option');
    optionElement.textContent = option;
    subDropdown.appendChild(optionElement);
  });
}

// Event listener for changes in the main dropdown
mainDropdown.addEventListener('change', populateSubDropdown);

// Populate the sub dropdown initially
populateSubDropdown();
