from numbers import Number

from repositories.customer_repository import Customer_Repository
from models.customer import Customer
from exceptions import DuplicateCustomerError, DuplicateCutomerError

class CustomerService:
    def __init__(self, repository: Customer_Repository):
        self._repository = repository

    def create_customer(self, customer: Customer) -> Customer:
        if self._repository.get_by_id(customer.id) is not None:
            raise DuplicateCustomerError(f"Customer with ID '{customer.id}' already exists.")
        return self._repository.add(customer)
    
    def get_all_customers(self) -> list[Customer]:
        return self._repository.get_all()
    
    def get_by_id(self, id: Number) -> Customer:
        return self._repository.get_by_id(id)
    
    def add_customer(self, customer: Customer) -> Customer:
        return self._repository.add(customer)
    
    def update_customer(self, customer: Customer) -> Customer:
        return self._repository.update(customer)
    
    def delete_customer(self, id: Number) -> None:
        self._repository.delete(id)