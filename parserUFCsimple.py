import lxml.html as html
from pandas import DataFrame

main_domain_stat = 'http://hosteddb.fightmetric.com'

page = html.parse(f'{main_domain_stat}/statistics/events/completed?page=all')

e = page.getroot().find_class('b-statistics__table-events').pop()

t = e.getchildren().pop()
event_tabl = DataFrame([{'EVENT':i[0].text_content().strip(), 'LINK':i[2]} for i in t.iterlinks()][1:])
event_date = DataFrame([{'EVENT': evt[0][0][0].text_content().strip(), 'DATE':evt[0][0][1].text_content().strip()} for evt in t.getchildren()[2:]])

sum_event = event_tabl.set_index('EVENT').join(event_date.set_index('EVENT')).reset_index()
sum_event.to_csv('./list.csv' , ';' , index=False)

all_fights = []
for i in sum_event.itertuples():
    page_event = html.parse(i[2])
    main_code = page_event.getroot()
    figth_event_tbl = main_code.find_class('b-fight-details__table-body').pop()[:]
    for figther_num in range(len(figth_event_tbl)):
        all_fights.append(
                        {'FIGHTER_WIN': figth_event_tbl[figther_num][1][0].text_content().strip(),
                        'FIGHTER_LOSE': figth_event_tbl[figther_num][1][1].text_content().strip(),
                        'METHOD': figth_event_tbl[figther_num][7][0].text_content().strip(),
                        'METHOD_DESC': figth_event_tbl[figther_num][7][1].text_content().strip(),
                        'ROUND': figth_event_tbl[figther_num][8][0].text_content().strip(),
                        'TIME': figth_event_tbl[figther_num][9][0].text_content().strip(),
                        'EVENT_NAME': i[1]}
                        )
history_stat = DataFrame(all_fights)
history_stat.to_csv('./list_result.csv' , ';' , index=False)

