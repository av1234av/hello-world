from Observer.kpis import KPIs
from Observer.currentkpis import CurrentKPIs
from Observer.forecastkpis import ForecastKPIs

#Report on current KPI values

with KPIs() as kpis:
    with CurrentKPIs(kpis), ForecastKPIs(kpis):
        kpis.set_kpis(25, 10, 5)
        kpis.set_kpis(100, 50, 30)
        kpis.set_kpis(50, 10, 20)

print('\n***Exited context managers ***\n')
kpis.set_kpis(150, 110, 120)