from ciu.cci.ControladorJogo import ControladorJogo
from ciu.cci.ControladorMenu import ControladorMenu
from edu.ControladorJogoEdu import ControladorJogoEdu

_author__ = 'Hanna e Neimar'

controlador = ControladorMenu(ControladorJogo())
controlador.menu()