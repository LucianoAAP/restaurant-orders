class TrackOrders:
    def __init__(self):
        self.orders = []
        self.orders_count = 0

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return self.orders_count

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])
        self.orders_count += 1

    def get_most_ordered_dish_per_customer(self, customer):
        customer_orders = {}
        for order in self.orders:
            if order[0] == customer:
                if order[1] in customer_orders:
                    customer_orders[order[1]] += 1
                else:
                    customer_orders[order[1]] = 1
        dishes = list(customer_orders.keys())
        counts = list(customer_orders.values())
        most_asked_count = max(counts)
        count_position = counts.index(most_asked_count)
        most_asked_dish = dishes[count_position]
        return most_asked_dish

    def get_never_ordered_per_customer(self, customer):
        total_dishes = set()
        dishes_ordered_by_customer = set()
        for order in self.orders:
            if order[1] not in total_dishes:
                total_dishes.add(order[1])
            if (
                order[0] == customer
                and order[1] not in dishes_ordered_by_customer
               ):
                dishes_ordered_by_customer.add(order[1])
        return total_dishes.difference(dishes_ordered_by_customer)

    def get_days_never_visited_per_customer(self, customer):
        every_day = set()
        days_with_customer = set()
        for order in self.orders:
            if order[2] not in every_day:
                every_day.add(order[2])
            if order[0] == customer and order[2] not in days_with_customer:
                days_with_customer.add(order[2])
        return every_day.difference(days_with_customer)

    def get_busiest_day(self):
        orders_by_day = {}
        for order in self.orders:
            if order[2] not in orders_by_day:
                orders_by_day[order[2]] = 1
            else:
                orders_by_day[order[2]] += 1
        counts = list(orders_by_day.values())
        most_orders = max(counts)
        days = list(orders_by_day.keys())
        highest_count_position = counts.index(most_orders)
        busiest_day = days[highest_count_position]
        return busiest_day

    def get_least_busy_day(self):
        orders_by_day = {}
        for order in self.orders:
            if order[2] not in orders_by_day:
                orders_by_day[order[2]] = 1
            else:
                orders_by_day[order[2]] += 1
        counts = list(orders_by_day.values())
        least_orders = min(counts)
        days = list(orders_by_day.keys())
        lowest_count_position = counts.index(least_orders)
        least_busy_day = days[lowest_count_position]
        return least_busy_day
