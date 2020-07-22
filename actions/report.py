def build_facility_report(self):
        print(f'     Aboretum: {self.name}')
        print(f'     Address: {self.address}')
        print(f'**** Rivers in ${self.name} ****')
        for river in self.rivers:
            print(f'River {river} [{str(river.id)[:8]}]')
            for animal in river.animals:
                print(f'    {animal}')
        print("Press any key to continue...")