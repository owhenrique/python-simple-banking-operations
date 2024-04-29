# Challenge: Create a banking system

## General purpose

Create a banking system with the following operations: withdraw, deposit and display statement.

## Challenge

We have been hired by a bank for develope its new system. The bank wanted to the upgrade its operations and chose the Python language to do so. For the first version, we only had to implement three operations: withdraw, deposit and statement.

## Operations

### Deposit Operation

It should be possible to deposit positive amounts into my account. The version of my first project only has one user, so we shouldn't have to implement the branch number and bank account number. All deposits should be stored in a variable and displayed in the statement operation.

#### Withdraw operation

The system must allow three withdrawals per day, with a limit of R$500 per withdrawal. If the user does not have the amount in their account, the system should display a message informing them that they cannot withdraw the amount due to insufficient funds. All withdrawals must be stored in a variable and displayed on the transaction statement.

### Statement operation

This operation should list all deposits and withdrawals made. At the end of the list, it should display the current funds in the account. 

The amounts should be printed in the format R$ XXX,XX, example: 1500,45 = R$ 1500,45