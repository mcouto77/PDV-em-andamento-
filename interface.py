from PyQt5 import uic, QtWidgets, QtCore, QtGui
from conexao import Conexao
#Função que insere código

class frenteCaixa:

    def consultaCodigo(self):

        codigo = pdv.inserir_codigo.text()
        consultados = Conexao()
        volta = consultados.ConsultarTabela(codigo)
        print(volta)

app = QtWidgets.QApplication([])
pdv = uic.loadUi("interface_2.ui")
tela_total = uic.loadUi("interface_total.ui")
dial_forma_pgto = uic.loadUi("dialogo_forma_pgto.ui")
pdv.inserir_codigo.returnPressed.connect(frenteCaixa.consultaCodigo)  # Utiliza o enter para enviar o código sem necessidade do pushButtom
#tela_total.lineEdit.returnPressed.connect(tela_pagamento)
#pdv.pushButton.clicked.connect(chamar_tela_pagamento)
#pdv.pushButton_2.clicked.connect(cancelar_produtos)
#pdv.pushButton_3.clicked.connect(forma_pagamento

pdv.showFullScreen()


pdv.show()
app.exec()
