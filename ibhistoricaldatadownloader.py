from time import sleep, strftime, localtime
from ib.ext.Contract import Contract
from ib.opt import ibConnection, message
import _mysql

new_symbolinput = ['MMM','ACE','AES','AFL','GAS','T','ABT','ANF','ACN','ADBE','AMD','AET','A','APD','ARG','AKAM','AA','ALXN','ATI','AGN','ALL','ANR','ALTR','MO','AMZN','AEE','AEP','AXP','AIG','AMT','AMP','ABC','AMGN','APH','APC','ADI','AON','APA','AIV','APOL','AAPL','AMAT','ADM','AIZ','AN','AZO','ADSK','ADP','AVB','AVY','AVP','BBT','BMC','BHI','BLL','BAC','BCR','BAX','BEAM','BDX','BBBY','BMS','BRK B','BBY','BIG','BIIB','BLK','HRB','BA','BWA','BXP','BSX','BMY','BRCM','BF B','CA','CBG','CBS','CF','CHRW','CMS','CNX','CSX','CVS','CVC','COG','CAM','CPB','COF','CAH','CFN','KMX','CCL','CAT','CELG','CNP','CTL','CERN','CHK','CVX','CME','CMG','CB','CI','CINF','CTAS','CSCO','C','CTXS','CLF','CLX','COH','KO','CCE','CTSH','CL','CMCSA','CMA','CSC','CAG','COP','ED','STZ','CBE','GLW','COST','CVH','COV','CCI','CMI','DTV','DTE','DHR','DRI','DVA','DV','DF','DE','DELL','DNR','XRAY','DVN','DO','DFS','DISCA','DLTR','D','RRD','DOV','DOW','DPS','DD','DUK','DNB','ETFC','EMC','EOG','EQT','EMN','ETN','ECL','EIX','EW','EA','EMR','ETR','EFX','EQR','EL','EXC','EXPE','EXPD','ESRX','XOM','FFIV','FLIR','FMC','FTI','FDO','FAST','FDX','FII','FIS','FITB','FHN','FSLR','FE','FISV','FLS','FLR','F','FRX','FOSL','BEN','FCX','FTR','GME','GCI','GPS','GD','GE','GIS','GPC','GNW','GILD','GS','GR','GT','GOOG','GWW','HCP','HAL','HOG','HAR','HRS','HIG','HAS','HCN','HNZ','HP','HSY','HES','HPQ','HD','HON','HRL','DHI','HSP','HST','HCBK','HUM','HBAN','ITW','IR','TEG','INTC','ICE','IPG','IBM','IFF','IGT','IP','INTU','ISRG','IVZ','IRM','JDSU','JPM','JBL','JEC','JNJ','JCI','JOY','JNPR','KLAC','K','KEY','KMB','KIM','KMI','KSS','KFT','KR','LLL','LSI','LH','LRCX','LM','LEG','LEN','LUK','LXK','LIFE','LLY','LTD','LNC','LLTC','LMT','L','LO','LOW','MTB','M','MRO','MPC','MAR','MMC','MAS','MA','MAT','MKC','MCD','MHP','MCK','MJN','MWV','MDT','MRK','MET','PCS','MCHP','MU','MSFT','MOLX','TAP','MON','MCO','MS','MOS','MSI','MUR','MYL','NKE','NRG','NYX','NBR','NDAQ','NOV','NTAP','NFLX','NWL','NFX','NEM','NWSA','NEE','NI','NE','NBL','JWN','NSC','NU','NTRS','NOC','NUE','NVDA','ORLY','OKE','OXY','OMC','ORCL','OI','PCAR','PCG','PNC','PPG','PPL','PLL','PH','PDCO','PAYX','BTU','JCP','PBCT','POM','PEP','PKI','PRGO','PFE','PM','PSX','PNW','PXD','PBI','PCL','PX','PCP','PCLN','PFG','PLD','PG','PGN','PGR','PRU','PEG','PSA','PHM','QEP','QCOM','PWR','DGX','RL','RRC','RTN','RHT','RF','RSG','RAI','RHI','ROK','COL','ROP','ROST','RDC','R','SAI','SCG','SLM','SWY','CRM','SNDK','SLE','SLB','SCHW','SNI','SEE','SHLD','SRE','SHW','SIAL','SPG','SJM','SNA','SO','LUV','SWN','SE','S','STJ','SWK','SPLS','SBUX','HOT','STT','SRCL','SYK','STI','SUN','SYMC','SYY','TROW','TEL','TE','TJX','TGT','THC','TDC','TER','TSO','TXN','TXT','BK','WMB','TMO','TIF','TWC','TWX','TIE','TMK','TSS','TRV','TRIP','TYC','TSN','USB','UNP','UPS','X','UTX','UNH','UNM','URBN','VFC','VLO','VAR','VTR','VRSN','VZ','VIAB','V','VNO','VMC','WPX','WMT','WAG','DIS','WPO','WM','WAT','WPI','WLP','WFC','WDC','WU','WY','WHR','WFM','WIN','WEC','WYN','WYNN','XL','XEL','XRX','XLNX','XYL','YHOO','YUM','ZMH','ZION','EBAY']
newDataList = []
dataDownload = []

def historical_data_handler(msg):
  global newDataList
  #print msg.reqId, msg.date, msg.open, msg.high, msg.low, msg.close, msg.volume
  if ('finished' in str(msg.date)) == False:
    new_symbol = new_symbolinput[msg.reqId]
    dataStr = '%s, %s, %s, %s, %s, %s, %s' % (new_symbol, strftime("%Y-%m-%d %H:%M:%S", localtime(int(msg.date))), msg.open, msg.high, msg.low, msg.close, msg.volume)
    newDataList = newDataList + [dataStr]
  else:
    new_symbol = new_symbolinput[msg.reqId]
    filename = 'minutetrades' + new_symbol + '.csv'
    csvfile = open('csv_day_test/' + filename,'wb')
    for item in newDataList:
      csvfile.write('%s \n' % item)
    csvfile.close()
    newDataList = []
    global dataDownload
    dataDownload.append(new_symbol)

con = ibConnection()
con.register(historical_data_handler, message.HistoricalData)
con.connect()

symbol_id = 0
for i in new_symbolinput:
  print i
  qqq = Contract()
  qqq.m_symbol = i
  qqq.m_secType = 'STK'
  qqq.m_exchange = 'SMART'
  qqq.m_currency = 'USD'
  con.reqHistoricalData(symbol_id, qqq, '', '1 D', '1 min', 'TRADES', 1, 2)

  symbol_id = symbol_id + 1
  sleep(10)

print dataDownload
filename = 'downloaded_symbols.csv'
csvfile = open('csv_day_test/' + filename,'wb')
for item in dataDownload:
  csvfile.write('%s \n' % item)
csvfile.close()
