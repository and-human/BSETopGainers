from kivy.metrics import dp
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from bsedata.bse import BSE


class BSETopGainersApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = FloatLayout()
        self.data_tables = MDDataTable(
            size_hint = (.9,1),
            use_pagination = False,
            check = False,
            column_data = [("Number", dp(20)), ("TICKER", dp(30)), ("LTP", dp(20)), ("ABS_CHANGE", dp(30)), ("PER_CHANGE", dp(30))],

            row_data = self.top_gainers_function(),
            sorted_on = "PER_CHANGE",
            elevation = 20
        )


    def build(self):
        """Here calling out layout variable, attaching layout type
        to bind it to the main app window"""
        self.layout.add_widget(self.data_tables)
        return self.layout

    """Main function that fetches the list of top_gainers.
    To Note - bsedata library scrapes data from the home page of markets,
    therefore there are only 5 items."""
    def top_gainers_function(self):

        bse = BSE()
        top_gainers = bse.topGainers()
        a = []
        for i in range(len(top_gainers)):
            ticker = top_gainers[i]["securityID"]
            ltp = top_gainers[i]["LTP"]
            abs_change = top_gainers[i]["change"]
            per_change = top_gainers[i]["pChange"]

            rowdata = [i+1, ticker, ltp, abs_change, per_change]

            a.append(rowdata)
        return a


if __name__ == "__main__":
    BSETopGainersApp().run()

