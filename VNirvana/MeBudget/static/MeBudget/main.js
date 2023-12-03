let earningAmount = document.getElementById("earning-amount");
let totalAmount = document.getElementById("total-amount");
let userAmount = document.getElementById("user-amount");
const earningAmountButton = document.getElementById("earning-amount-button");
const checkAmountButton = document.getElementById("check-amount");
const totalAmountButton = document.getElementById("total-amount-button");
const productTitle = document.getElementById("product-title");
const earningErrorMessage = document.getElementById("earning-error");
const errorMessage = document.getElementById("budget-error");
const productTitleError = document.getElementById("product-title-error");
const productCostError = document.getElementById("product-cost-error");
const earningValue = document.getElementById("earning-value");
const amount = document.getElementById("amount");
const expenditureValue = document.getElementById("expenditure-value");
const balanceValue = document.getElementById("balance-amount");
const list = document.getElementById("list");
let tempAmount = 0;

// Set Budget Part
totalAmountButton.addEventListener("click", (e) => {
  e.preventDefault();
  tempAmount = totalAmount.value;
  if (tempAmount === "" || tempAmount < 0) {
    errorMessage.classList.remove("hide");
  } else {
    errorMessage.classList.add("hide");
    amount.innerHTML = tempAmount;
    balanceValue.innerText = tempAmount;
    totalAmount.value = "";
  }
});

// Set Earnings Part
earningAmountButton.addEventListener("click", (e) => {
  e.preventDefault();
  let earning = parseInt(earningAmount.value);
  if (!isNaN(earning)) {
    let currentEarnings = parseInt(earningValue.innerText);
    earningValue.innerText = currentEarnings + earning;
    let currentBalance = parseInt(balanceValue.innerText);
    balanceValue.innerText = currentBalance + earning;
    earningAmount.value = "";
    earningErrorMessage.classList.add("hide");
  } else {
    earningErrorMessage.classList.remove("hide");
  }
});


// Function To Disable Edit and Delete Button
const disableButtons = (bool) => {
  let editButtons = document.getElementsByClassName("edit");
  Array.from(editButtons).forEach((element) => {
    element.disabled = bool;
  });
};

// Function To Modify List Elements
const modifyElement = (element, edit = false) => {
let parentDiv = element.parentElement;
let currentEarning = earningValue.innerText
let currentBalance = balanceValue.innerText;
let currentExpense = expenditureValue.innerText;
let parentAmount = parentDiv.querySelector(".amount").innerText;
if (edit) {
    let parentText = parentDiv.querySelector(".product").innerText;
    productTitle.value = parentText;
    userAmount.value = parentAmount;
    disableButtons(true);
}
balanceValue.innerText = parseInt(currentBalance) + parseInt(parentAmount);
expenditureValue.innerText =
    parseInt(currentExpense) - parseInt(parentAmount);
parentDiv.remove();
};

// Function To Create List
const listCreator = (expenseName, expenseValue) => {
    let sublistContent = document.createElement("div");
  sublistContent.classList.add("sublist-content", "flex-space");
  list.appendChild(sublistContent);
  sublistContent.innerHTML = `<p class="product">${expenseName}</p><p class="amount">${expenseValue}</p>`;
  let editButton = document.createElement("button");
  editButton.classList.add("fa-solid", "fa-pen-to-square", "edit");
  editButton.style.fontSize = "1.2em";
  editButton.addEventListener("click", () => {
    modifyElement(editButton, true);
  });
  let deleteButton = document.createElement("button");
  deleteButton.classList.add("fa-solid", "fa-trash-can", "delete");
  deleteButton.style.fontSize = "1.2em";
  deleteButton.addEventListener("click", () => {
    modifyElement(deleteButton);
  });
  sublistContent.appendChild(editButton);
  sublistContent.appendChild(deleteButton);
  document.getElementById("list").appendChild(sublistContent);
};

// Function To Add Expenses
checkAmountButton.addEventListener("click", (e) => { 
  e.preventDefault();
  // Empty checks
  if (!userAmount.value || !productTitle.value) {
    productTitleError.classList.remove("hide");
    return false;
  }
  // Enable buttons
  disableButtons(false);
  // Expense
  let expenditure = parseInt(userAmount.value);
  // Total expense (existing + new)
  let currentExpenses = parseInt(expenditureValue.innerText);
  let sum = currentExpenses + expenditure;
  expenditureValue.innerText = sum;
  // Total balance (budget + total earnings - total expense)
  let currentEarnings = parseInt(earningValue.innerText);
  const totalBalance = (parseInt(tempAmount) + parseInt(currentEarnings)) - parseInt(sum);
  balanceValue.innerText = totalBalance;
  // Create list
  listCreator(productTitle.value, userAmount.value);

  // Empty inputs
  productTitle.value = "";
  userAmount.value = "";
});
