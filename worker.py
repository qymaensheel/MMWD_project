class Worker:
    occupied_ID = []

    def __init__(self, cl_list, rest_list):
        if self.occupied_ID == []:
            self.ID = 1
        else:
            self.ID = self.occupied_ID[-1] + 1
        self.occupied_ID.append(self.ID)
        self.clients_list = cl_list.copy()
        self.restautants_list = rest_list.copy()
