# imports application from folder
from portfolio import app

if __name__ == '__main__':
    app.run(debug = True, host='localhost', port =5555)
    ## FOR DEBUG: debug= True
    ## HOST IS LOCAL HOST, WHICH IS YOUR LOCAL COMPUTER
    ## TO CHOOSE A PORT NUMBER: port=5555
    #*** HOST AND PORT CASE SENSITIVE