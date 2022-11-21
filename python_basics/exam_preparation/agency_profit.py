company_name = input()
number_tickets_adults = int(input())
number_child_tickets = int(input())
net_price_ticket = float(input())
tax_service = float(input())

net_price_child = net_price_ticket * 0.30
price_ticket_adult_tax = net_price_ticket + tax_service

price_child_with_tax = net_price_child + tax_service

all_price_tickets = (number_child_tickets * price_child_with_tax) + (number_tickets_adults * price_ticket_adult_tax)

profit = all_price_tickets * 0.20

print(f"The profit of your agency from {company_name} tickets is {profit:.2f} lv.")
