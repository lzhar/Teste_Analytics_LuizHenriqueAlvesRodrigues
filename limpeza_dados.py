from datetime import datetime as date
from decimal import Decimal, ROUND_DOWN

class Produto:

    def __init__(self, id, nome, categoria, preco):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.preco = preco



class Dados:

    def __init__(self, id, data, produto, quantidade):
        self.id = id
        self.data = data
        self.produto = produto
        self.quantidade = quantidade

    
    def montar_dados(self): 


        produto1 = Produto(1, "Paracetamol 500mg", "Medicamentos", 7.5000)
        produto2 = Produto(2, "Dipirona 500mg", "Medicamentos", 5.9090)
        produto3 = Produto(3, "Ibuprofeno 400mg", "Medicamentos", 8.9098)
        produto4 = Produto(4, "Sabonete Lux", "Produtos de higiene pessoal", 3.5013)
        produto5 = Produto(5, "Shampoo Seda", "Produtos de higiene pessoal", 9.9543)
        produto6 = Produto(6, "Creme Dental Colgate", "Produtos de higiene pessoal", 6.95098)
        produto7 = Produto(7, "Batom Maybelline", "Produtos de beleza", 29.9012)
        produto8 = Produto(8, "Base Vult", "Produtos de beleza", 35.9032)
        produto9 = Produto(9, "Perfume Natura", "Não consta", 89.993232)
        produto10 = Produto(10, "", "Produtos de bem-estar", 29.9099)
        produto11 = Produto(11, "Ômega 3 Sundown", "Produtos de bem-estar", 49.90332)
        produto12 = Produto(12, "Chá de Camomila", "Produtos de bem-estar", 4.9012)
        produto13 = Produto(13, "Fralda Pampers Confort Sec G", "Produtos para bebês", 189.9032)
        produto14 = Produto(14, "Lenço Umedecido Huggies", "Produtos para bebês", 9.90323)
        produto15 = Produto(15, "Fórmula Infantil Nan", "Produtos para bebês", 39.90323)
        produto16 = Produto(16, "Gaze Estéril", "Produtos hospitalares e de primeiros socorros", 6.90213)
        produto17 = Produto(17, "Álcool 70%", "Produtos hospitalares e de primeiros socorros", 3.903232)
        produto18 = Produto(18, "Termômetro Digital", "Produtos hospitalares e de primeiros socorros", 45.9032)
        produto19 = Produto(19, "Chocolate Snickers", "Produtos de conveniência", 5.49233)
        produto20 = Produto(20, "Biscoito Oreo", "Produtos de conveniência", 6.90323)
        produto21 = Produto(21, "Suco de Laranja Del Valle", "Produtos de conveniência", 4.90323)

        
        dados_um = Dados(1, date(2023, 1, 1), produto10, 4)
        dados_dois = Dados(2, date(2023, 1, 1), produto3, 12)
        dados_tres = Dados(3, date(2023, 1, 1), produto7, 7)
        dados_quatro = Dados(4, date(2023, 1, 2), produto14, 19)
        dados_cinco = Dados(5, date(2023, 1, 2), produto1, 25)
        dados_seis = Dados(6, date(2023, 1, 3), produto9, 3)
        dados_sete = Dados(7, date(2023, 1, 3), produto12, 44)
        dados_oito = Dados(8, date(2023, 1, 4), produto5, 6)
        dados_nove = Dados(9, date(2023, 1, 4), produto18, 18)
        dados_dez = Dados(10, date(2023, 1, 5), produto2, 9)
        dados_onze = Dados(11, date(2023, 1, 5), produto20, 30)
        dados_doze = Dados(12, date(2023, 1, 6), produto6, 15)
        dados_treze = Dados(13, date(2023, 1, 7), produto8, 21)
        dados_quatorze = Dados(14, date(2023, 1, 7), produto17, 2)
        dados_quinze = Dados(15, date(2023, 1, 8), produto11, 50)
        dados_dezesseis = Dados(16, date(2023, 1, 8), produto4, 33)
        dados_dezessete = Dados(17, date(2023, 1, 9), produto15, 11)
        dados_dezoito = Dados(18, date(2023, 1, 10), produto19, 14)
        dados_dezenove = Dados(19, date(2023, 1, 10), produto13, 20)
        dados_vinte = Dados(20, date(2023, 1, 11), produto1, 5)

        dados_vinte_um = Dados(21, date(2023, 1, 11), produto3, 8)
        dados_vinte_dois = Dados(22, date(2023, 1, 12), produto6, 40)
        dados_vinte_tres = Dados(23, date(2023, 1, 13), produto10, 12)
        dados_vinte_quatro = Dados(24, date(2023, 1, 13), produto2, 28)
        dados_vinte_cinco = Dados(25, date(2023, 1, 14), produto7, 22)
        dados_vinte_seis = Dados(26, date(2023, 1, 15), produto9, 9)
        dados_vinte_sete = Dados(27, date(2023, 1, 15), produto12, 37)
        dados_vinte_oito = Dados(28, date(2023, 1, 16), produto5, 4)
        dados_vinte_nove = Dados(29, date(2023, 1, 16), produto18, 26)
        dados_trinta = Dados(30, date(2023, 1, 17), produto14, 13)
        dados_trinta_um = Dados(31, date(2023, 1, 17), produto20, 31)
        dados_trinta_dois = Dados(32, date(2023, 1, 18), produto6, 2)
        dados_trinta_tres = Dados(33, date(2023, 1, 18), produto8, 44)
        dados_trinta_quatro = Dados(34, date(2023, 1, 19), produto17, 7)
        dados_trinta_cinco = Dados(35, date(2023, 1, 20), produto11, 19)
        dados_trinta_seis = Dados(36, date(2023, 1, 20), produto4, 10)
        dados_trinta_sete = Dados(37, date(2023, 1, 21), produto15, 36)
        dados_trinta_oito = Dados(38, date(2023, 1, 21), produto19, 5)
        dados_trinta_nove = Dados(39, date(2023, 1, 22), produto13, 27)
        dados_quarenta = Dados(40, date(2023, 1, 23), produto1, 1)

        dados_quarenta_um = Dados(41, date(2023, 1, 23), produto3, 48)
        dados_quarenta_dois = Dados(42, date(2023, 1, 24), produto6, 15)
        dados_quarenta_tres = Dados(43, date(2023, 1, 25), produto10, 23)
        dados_quarenta_quatro = Dados(44, date(2023, 1, 25), produto2, 6)
        dados_quarenta_cinco = Dados(45, date(2023, 1, 26), produto7, 35)
        dados_quarenta_seis = Dados(46, date(2023, 1, 27), produto9, 17)
        dados_quarenta_sete = Dados(47, date(2023, 1, 27), produto12, 9)
        dados_quarenta_oito = Dados(48, date(2023, 1, 28), produto5, 41)
        dados_quarenta_nove = Dados(49, date(2023, 1, 29), produto18, 14)
        dados_cinquenta = Dados(50, date(2023, 1, 29), produto14, 8)
        dados_cinquenta_um = Dados(51, date(2023, 1, 30), produto20, 30)
        dados_cinquenta_dois = Dados(52, date(2023, 1, 30), produto6, 4)
        dados_cinquenta_tres = Dados(53, date(2023, 1, 31), produto8, 12)
        dados_cinquenta_quatro = Dados(54, date(2023, 1, 31), produto17, 47)
        dados_cinquenta_cinco = Dados(55, date(2023, 1, 31), produto11, 20)
        dados_cinquenta_seis = Dados(56, date(2023, 1, 31), produto4, 16)
        dados_cinquenta_sete = Dados(57, date(2023, 1, 31), produto15, 7)
        dados_cinquenta_oito = Dados(58, date(2023, 1, 31), produto19, 29)
        dados_cinquenta_nove = Dados(59, date(2023, 1, 31), produto13, 3)
        dados_sessenta = Dados(60, date(2023, 1, 31), produto1, 10)
        
        dados_sessenta_e_um = Dados(61, date(2023, 2, 1), produto2, 14)
        dados_sessenta_e_dois = Dados(62, date(2023, 2, 1), produto5, 8)
        dados_sessenta_e_tres = Dados(63, date(2023, 2, 1), produto7, 22)
        dados_sessenta_e_quatro = Dados(64, date(2023, 2, 2), produto1, 19)
        dados_sessenta_e_cinco = Dados(65, date(2023, 2, 2), produto3, 31)
        dados_sessenta_e_seis = Dados(66, date(2023, 2, 3), produto6, 5)
        dados_sessenta_e_sete = Dados(67, date(2023, 2, 3), produto8, 12)
        dados_sessenta_e_oito = Dados(68, date(2023, 2, 3), produto10, 28)
        dados_sessenta_e_nove = Dados(69, date(2023, 2, 4), produto12, 7)
        dados_setenta = Dados(70, date(2023, 2, 4), produto14, 24)
        dados_setenta_e_um = Dados(71, date(2023, 2, 5), produto9, 11)
        dados_setenta_e_dois = Dados(72, date(2023, 2, 5), produto11, 16)
        dados_setenta_e_tres = Dados(73, date(2023, 2, 6), produto13, 21)
        dados_setenta_e_quatro = Dados(74, date(2023, 2, 6), produto15, 9)
        dados_setenta_e_cinco = Dados(75, date(2023, 2, 7), produto17, 33)
        dados_setenta_e_seis = Dados(76, date(2023, 2, 7), produto19, 4)
        dados_setenta_e_sete = Dados(77, date(2023, 2, 8), produto20, 18)
        dados_setenta_e_oito = Dados(78, date(2023, 2, 8), produto2, 13)
        dados_setenta_e_nove = Dados(79, date(2023, 2, 9), produto5, 27)

        dados_oitenta = Dados(80, date(2023, 2, 9), produto7, 6)
        dados_oitenta_e_um = Dados(81, date(2023, 2, 10), produto1, 29)
        dados_oitenta_e_dois = Dados(82, date(2023, 2, 10), produto3, 10)
        dados_oitenta_e_tres = Dados(83, date(2023, 2, 11), produto6, 22)
        dados_oitenta_e_quatro = Dados(84, date(2023, 2, 11), produto8, 17)
        dados_oitenta_e_cinco = Dados(85, date(2023, 2, 12), produto10, 8)
        dados_oitenta_e_seis = Dados(86, date(2023, 2, 12), produto12, 25)
        dados_oitenta_e_sete = Dados(87, date(2023, 2, 13), produto14, 12)
        dados_oitenta_e_oito = Dados(88, date(2023, 2, 13), produto9, 19)
        dados_oitenta_e_nove = Dados(89, date(2023, 2, 14), produto11, 15)
        dados_noventa = Dados(90, date(2023, 2, 14), produto13, 23)
        dados_noventa_e_um = Dados(91, date(2023, 2, 15), produto15, 7)
        dados_noventa_e_dois = Dados(92, date(2023, 2, 15), produto17, 32)
        dados_noventa_e_tres = Dados(93, date(2023, 2, 16), produto19, 5)
        dados_noventa_e_quatro = Dados(94, date(2023, 2, 16), produto20, 14)
        dados_noventa_e_cinco = Dados(95, date(2023, 2, 17), produto2, 26)
        dados_noventa_e_seis = Dados(96, date(2023, 2, 17), produto5, 9)
        dados_noventa_e_sete = Dados(97, date(2023, 2, 18), produto7, 21)
        dados_noventa_e_oito = Dados(98, date(2023, 2, 18), produto1, 11)
        dados_noventa_e_nove = Dados(99, date(2023, 2, 19), produto3, 30)
        dados_cem = Dados(100, date(2023, 2, 19), produto6, 8)

        dados_cento_e_um = Dados(101, date(2023, 2, 20), produto8, 17)
        dados_cento_e_dois = Dados(102, date(2023, 2, 20), produto10, 4)
        dados_cento_e_tres = Dados(103, date(2023, 2, 21), produto12, 28)
        dados_cento_e_quatro = Dados(104, date(2023, 2, 21), produto14, 13)
        dados_cento_e_cinco = Dados(105, date(2023, 2, 22), produto9, 16)
        dados_cento_e_seis = Dados(106, date(2023, 2, 22), produto11, 6)
        dados_cento_e_sete = Dados(107, date(2023, 2, 23), produto13, 24)
        dados_cento_e_oito = Dados(108, date(2023, 2, 23), produto15, 12)
        dados_cento_e_nove = Dados(109, date(2023, 2, 24), produto17, 7)
        dados_cento_e_dez = Dados(110, date(2023, 2, 24), produto19, 20)
        dados_cento_e_onze = Dados(111, date(2023, 2, 25), produto20, 10)
        dados_cento_e_doze = Dados(112, date(2023, 2, 25), produto2, 31)
        dados_cento_e_treze = Dados(113, date(2023, 2, 26), produto5, 15)
        dados_cento_e_quatorze = Dados(114, date(2023, 2, 26), produto7, 22)
        dados_cento_e_quinze = Dados(115, date(2023, 2, 27), produto1, 8)
        dados_cento_e_dezesseis = Dados(116, date(2023, 2, 27), produto3, 19)
        dados_cento_e_dezessete = Dados(117, date(2023, 2, 28), produto6, 11)
        dados_cento_e_dezoito = Dados(118, date(2023, 2, 28), produto8, 26)
        dados_cento_e_dezenove = Dados(119, date(2023, 2, 28), produto10, 5)
        dados_cento_e_vinte = Dados(120, date(2023, 2, 28), produto12, 18)

        dados_cento_e_vinte_e_um = Dados(121, date(2023, 3, 1), produto1, 12)
        dados_cento_e_vinte_e_dois = Dados(122, date(2023, 3, 1), produto3, 25)
        dados_cento_e_vinte_e_tres = Dados(123, date(2023, 3, 2), produto5, 7)
        dados_cento_e_vinte_e_quatro = Dados(124, date(2023, 3, 2), produto7, 18)
        dados_cento_e_vinte_e_cinco = Dados(125, date(2023, 3, 3), produto2, 30)
        dados_cento_e_vinte_e_seis = Dados(126, date(2023, 3, 3), produto4, 9)
        dados_cento_e_vinte_e_sete = Dados(127, date(2023, 3, 3), produto6, 22)
        dados_cento_e_vinte_e_oito = Dados(128, date(2023, 3, 4), produto8, 15)
        dados_cento_e_vinte_e_nove = Dados(129, date(2023, 3, 4), produto10, 31)
        dados_cento_e_trinta = Dados(130, date(2023, 3, 5), produto12, 11)
        dados_cento_e_trinta_e_um = Dados(131, date(2023, 3, 5), produto14, 24)
        dados_cento_e_trinta_e_dois = Dados(132, date(2023, 3, 6), produto9, 6)
        dados_cento_e_trinta_e_tres = Dados(133, date(2023, 3, 6), produto11, 20)
        dados_cento_e_trinta_e_quatro = Dados(134, date(2023, 3, 7), produto13, 14)
        dados_cento_e_trinta_e_cinco = Dados(135, date(2023, 3, 7), produto15, 27)
        dados_cento_e_trinta_e_seis = Dados(136, date(2023, 3, 8), produto17, 5)
        dados_cento_e_trinta_e_sete = Dados(137, date(2023, 3, 8), produto19, 19)
        dados_cento_e_trinta_e_oito = Dados(138, date(2023, 3, 9), produto20, 8)
        dados_cento_e_trinta_e_nove = Dados(139, date(2023, 3, 9), produto1, 21)
        
        dados_cento_e_quarenta = Dados(140, date(2023, 3, 10), produto3, 13)
        dados_cento_e_quarenta_e_um = Dados(141, date(2023, 3, 10), produto5, 30)
        dados_cento_e_quarenta_e_dois = Dados(142, date(2023, 3, 11), produto7, 7)
        dados_cento_e_quarenta_e_tres = Dados(143, date(2023, 3, 11), produto2, 26)
        dados_cento_e_quarenta_e_quatro = Dados(144, date(2023, 3, 12), produto4, 10)
        dados_cento_e_quarenta_e_cinco = Dados(145, date(2023, 3, 12), produto6, 29)
        dados_cento_e_quarenta_e_seis = Dados(146, date(2023, 3, 13), produto8, 12)
        dados_cento_e_quarenta_e_sete = Dados(147, date(2023, 3, 13), produto10, 22)
        dados_cento_e_quarenta_e_oito = Dados(148, date(2023, 3, 14), produto12, 3)
        dados_cento_e_quarenta_e_nove = Dados(149, date(2023, 3, 14), produto14, 24)
        dados_cento_e_cinquenta = Dados(150, date(2023, 3, 15), produto9, 9)
        dados_cento_e_cinquenta_e_um = Dados(151, date(2023, 3, 15), produto11, 31)
        dados_cento_e_cinquenta_e_dois = Dados(152, date(2023, 3, 16), produto13, 16)
        dados_cento_e_cinquenta_e_tres = Dados(153, date(2023, 3, 16), produto15, 5)
        dados_cento_e_cinquenta_e_quatro = Dados(154, date(2023, 3, 17), produto17, 27)
        dados_cento_e_cinquenta_e_cinco = Dados(155, date(2023, 3, 17), produto19, 6)
        dados_cento_e_cinquenta_e_seis = Dados(156, date(2023, 3, 18), produto20, 19)
        dados_cento_e_cinquenta_e_sete = Dados(157, date(2023, 3, 18), produto1, 10)
        dados_cento_e_cinquenta_e_oito = Dados(158, date(2023, 3, 19), produto3, 23)
        dados_cento_e_cinquenta_e_nove = Dados(159, date(2023, 3, 19), produto5, 12)
        
        dados_cento_e_sessenta = Dados(160, date(2023, 3, 20), produto7, 29)
        dados_cento_e_sessenta_e_um = Dados(161, date(2023, 3, 20), produto2, 4)
        dados_cento_e_sessenta_e_dois = Dados(162, date(2023, 3, 21), produto4, 21)
        dados_cento_e_sessenta_e_tres = Dados(163, date(2023, 3, 21), produto6, 8)
        dados_cento_e_sessenta_e_quatro = Dados(164, date(2023, 3, 22), produto8, 18)
        dados_cento_e_sessenta_e_cinco = Dados(165, date(2023, 3, 22), produto10, 5)
        dados_cento_e_sessenta_e_seis = Dados(166, date(2023, 3, 23), produto12, 27)
        dados_cento_e_sessenta_e_sete = Dados(167, date(2023, 3, 23), produto14, 14)
        dados_cento_e_sessenta_e_oito = Dados(168, date(2023, 3, 24), produto9, 22)
        dados_cento_e_sessenta_e_nove = Dados(169, date(2023, 3, 24), produto11, 7)
        dados_cento_e_setenta = Dados(170, date(2023, 3, 25), produto13, 30)
        dados_cento_e_setenta_e_um = Dados(171, date(2023, 3, 25), produto15, 11)
        dados_cento_e_setenta_e_dois = Dados(172, date(2023, 3, 26), produto17, 19)
        dados_cento_e_setenta_e_tres = Dados(173, date(2023, 3, 26), produto19, 6)
        dados_cento_e_setenta_e_quatro = Dados(174, date(2023, 3, 27), produto20, 23)
        dados_cento_e_setenta_e_cinco = Dados(175, date(2023, 3, 27), produto1, 9)
        dados_cento_e_setenta_e_seis = Dados(176, date(2023, 3, 28), produto3, 26)
        dados_cento_e_setenta_e_sete = Dados(177, date(2023, 3, 28), produto5, 13)
        dados_cento_e_setenta_e_oito = Dados(178, date(2023, 3, 29), produto7, 18)
        dados_cento_e_setenta_e_nove = Dados(179, date(2023, 3, 29), produto2, 4)
        dados_cento_e_oitenta = Dados(180, date(2023, 3, 30), produto4, 28)

        dados_cento_e_oitenta_e_um = Dados(181, date(2023, 4, 1), produto2, 14)
        dados_cento_e_oitenta_e_dois = Dados(182, date(2023, 4, 1), produto4, 27)
        dados_cento_e_oitenta_e_tres = Dados(183, date(2023, 4, 2), produto6, 9)
        dados_cento_e_oitenta_e_quatro = Dados(184, date(2023, 4, 2), produto8, 21)
        dados_cento_e_oitenta_e_cinco = Dados(185, date(2023, 4, 3), produto10, 5)
        dados_cento_e_oitenta_e_seis = Dados(186, date(2023, 4, 3), produto12, 18)
        dados_cento_e_oitenta_e_sete = Dados(187, date(2023, 4, 3), produto14, 24)
        dados_cento_e_oitenta_e_oito = Dados(188, date(2023, 4, 4), produto16, 11)
        dados_cento_e_oitenta_e_nove = Dados(189, date(2023, 4, 4), produto18, 30)
        dados_cento_e_noventa = Dados(190, date(2023, 4, 5), produto20, 7)
        dados_cento_e_noventa_e_um = Dados(191, date(2023, 4, 5), produto1, 25)
        dados_cento_e_noventa_e_dois = Dados(192, date(2023, 4, 6), produto3, 12)
        dados_cento_e_noventa_e_tres = Dados(193, date(2023, 4, 6), produto5, 28)
        dados_cento_e_noventa_e_quatro = Dados(194, date(2023, 4, 7), produto7, 4)
        dados_cento_e_noventa_e_cinco = Dados(195, date(2023, 4, 7), produto9, 17)
        dados_cento_e_noventa_e_seis = Dados(196, date(2023, 4, 8), produto11, 22)
        dados_cento_e_noventa_e_sete = Dados(197, date(2023, 4, 8), produto13, 8)
        dados_cento_e_noventa_e_oito = Dados(198, date(2023, 4, 9), produto15, 19)
        dados_cento_e_noventa_e_nove = Dados(199, date(2023, 4, 9), produto17, 6)
        
        dados_duzentos = Dados(200, date(2023, 4, 10), produto19, 26)
        dados_duzentos_e_um = Dados(201, date(2023, 4, 10), produto2, 10)
        dados_duzentos_e_dois = Dados(202, date(2023, 4, 11), produto4, 14)
        dados_duzentos_e_tres = Dados(203, date(2023, 4, 11), produto6, 29)
        dados_duzentos_e_quatro = Dados(204, date(2023, 4, 12), produto8, 3)
        dados_duzentos_e_cinco = Dados(205, date(2023, 4, 12), produto10, 21)
        dados_duzentos_e_seis = Dados(206, date(2023, 4, 13), produto12, 7)
        dados_duzentos_e_sete = Dados(207, date(2023, 4, 13), produto14, 24)
        dados_duzentos_e_oito = Dados(208, date(2023, 4, 14), produto16, 5)
        dados_duzentos_e_nove = Dados(209, date(2023, 4, 14), produto18, 20)
        dados_duzentos_e_dez = Dados(210, date(2023, 4, 15), produto20, 12)
        dados_duzentos_e_onze = Dados(211, date(2023, 4, 15), produto1, 27)
        dados_duzentos_e_doze = Dados(212, date(2023, 4, 16), produto3, 8)
        dados_duzentos_e_treze = Dados(213, date(2023, 4, 16), produto5, 23)
        dados_duzentos_e_quatorze = Dados(214, date(2023, 4, 17), produto7, 16)
        dados_duzentos_e_quinze = Dados(215, date(2023, 4, 17), produto9, 30)
        dados_duzentos_e_dezesseis = Dados(216, date(2023, 4, 18), produto11, 4)
        dados_duzentos_e_dezessete = Dados(217, date(2023, 4, 18), produto13, 18)
        dados_duzentos_e_dezoito = Dados(218, date(2023, 4, 19), produto15, 11)
        dados_duzentos_e_dezenove = Dados(219, date(2023, 4, 19), produto17, 28)
        
        dados_duzentos_e_vinte = Dados(220, date(2023, 4, 20), produto19, 9)
        dados_duzentos_e_vinte_e_um = Dados(221, date(2023, 4, 20), produto2, 26)
        dados_duzentos_e_vinte_e_dois = Dados(222, date(2023, 4, 21), produto4, 15)
        dados_duzentos_e_vinte_e_tres = Dados(223, date(2023, 4, 21), produto6, 19)
        dados_duzentos_e_vinte_e_quatro = Dados(224, date(2023, 4, 22), produto8, 7)
        dados_duzentos_e_vinte_e_cinco = Dados(225, date(2023, 4, 22), produto10, 23)
        dados_duzentos_e_vinte_e_seis = Dados(226, date(2023, 4, 23), produto12, 6)
        dados_duzentos_e_vinte_e_sete = Dados(227, date(2023, 4, 23), produto14, 25)
        dados_duzentos_e_vinte_e_oito = Dados(228, date(2023, 4, 24), produto16, 13)
        dados_duzentos_e_vinte_e_nove = Dados(229, date(2023, 4, 24), produto18, 30)
        dados_duzentos_e_trinta = Dados(230, date(2023, 4, 25), produto20, 8)
        dados_duzentos_e_trinta_e_um = Dados(231, date(2023, 4, 25), produto1, 17)
        dados_duzentos_e_trinta_e_dois = Dados(232, date(2023, 4, 26), produto3, 22)
        dados_duzentos_e_trinta_e_tres = Dados(233, date(2023, 4, 26), produto5, 10)
        dados_duzentos_e_trinta_e_quatro = Dados(234, date(2023, 4, 27), produto7, 27)
        dados_duzentos_e_trinta_e_cinco = Dados(235, date(2023, 4, 27), produto9, 12)
        dados_duzentos_e_trinta_e_seis = Dados(236, date(2023, 4, 28), produto11, 20)
        dados_duzentos_e_trinta_e_sete = Dados(237, date(2023, 4, 28), produto13, 5)
        dados_duzentos_e_trinta_e_oito = Dados(238, date(2023, 4, 29), produto15, 29)
        dados_duzentos_e_trinta_e_nove = Dados(239, date(2023, 4, 29), produto17, 14)
        dados_duzentos_e_quarenta = Dados(240, date(2023, 4, 29), produto19, 11)

        dados_duzentos_e_quarenta_e_um = Dados(241, date(2023, 5, 1), produto2, 16)
        dados_duzentos_e_quarenta_e_dois = Dados(242, date(2023, 5, 1), produto4, 28)
        dados_duzentos_e_quarenta_e_tres = Dados(243, date(2023, 5, 2), produto6, 9)
        dados_duzentos_e_quarenta_e_quatro = Dados(244, date(2023, 5, 2), produto8, 25)
        dados_duzentos_e_quarenta_e_cinco = Dados(245, date(2023, 5, 3), produto10, 12)
        dados_duzentos_e_quarenta_e_seis = Dados(246, date(2023, 5, 3), produto12, 19)
        dados_duzentos_e_quarenta_e_sete = Dados(247, date(2023, 5, 4), produto14, 27)
        dados_duzentos_e_quarenta_e_oito = Dados(248, date(2023, 5, 4), produto16, 8)
        dados_duzentos_e_quarenta_e_nove = Dados(249, date(2023, 5, 5), produto18, 30)
        dados_duzentos_e_cinquenta = Dados(250, date(2023, 5, 5), produto20, 11)
        dados_duzentos_e_cinquenta_e_um = Dados(251, date(2023, 5, 6), produto1, 24)
        dados_duzentos_e_cinquenta_e_dois = Dados(252, date(2023, 5, 6), produto3, 7)
        dados_duzentos_e_cinquenta_e_tres = Dados(253, date(2023, 5, 7), produto5, 22)
        dados_duzentos_e_cinquenta_e_quatro = Dados(254, date(2023, 5, 7), produto7, 14)
        dados_duzentos_e_cinquenta_e_cinco = Dados(255, date(2023, 5, 8), produto9, 18)
        dados_duzentos_e_cinquenta_e_seis = Dados(256, date(2023, 5, 8), produto11, 29)
        dados_duzentos_e_cinquenta_e_sete = Dados(257, date(2023, 5, 9), produto13, 5)
        dados_duzentos_e_cinquenta_e_oito = Dados(258, date(2023, 5, 9), produto15, 20)
        dados_duzentos_e_cinquenta_e_nove = Dados(259, date(2023, 5, 10), produto17, 15)
        
        dados_duzentos_e_sessenta = Dados(260, date(2023, 5, 10), produto19, 26)
        dados_duzentos_e_sessenta_e_um = Dados(261, date(2023, 5, 11), produto2, 13)
        dados_duzentos_e_sessenta_e_dois = Dados(262, date(2023, 5, 11), produto4, 21)
        dados_duzentos_e_sessenta_e_tres = Dados(263, date(2023, 5, 12), produto6, 30)
        dados_duzentos_e_sessenta_e_quatro = Dados(264, date(2023, 5, 12), produto8, 6)
        dados_duzentos_e_sessenta_e_cinco = Dados(265, date(2023, 5, 13), produto10, 19)
        dados_duzentos_e_sessenta_e_seis = Dados(266, date(2023, 5, 13), produto12, 9)
        dados_duzentos_e_sessenta_e_sete = Dados(267, date(2023, 5, 14), produto14, 24)
        dados_duzentos_e_sessenta_e_oito = Dados(268, date(2023, 5, 14), produto16, 11)
        dados_duzentos_e_sessenta_e_nove = Dados(269, date(2023, 5, 15), produto18, 17)
        dados_duzentos_e_setenta = Dados(270, date(2023, 5, 15), produto20, 28)
        dados_duzentos_e_setenta_e_um = Dados(271, date(2023, 5, 16), produto1, 7)
        dados_duzentos_e_setenta_e_dois = Dados(272, date(2023, 5, 16), produto3, 23)
        dados_duzentos_e_setenta_e_tres = Dados(273, date(2023, 5, 17), produto5, 16)
        dados_duzentos_e_setenta_e_quatro = Dados(274, date(2023, 5, 17), produto7, 27)
        dados_duzentos_e_setenta_e_cinco = Dados(275, date(2023, 5, 18), produto9, 4)
        dados_duzentos_e_setenta_e_seis = Dados(276, date(2023, 5, 18), produto11, 22)
        dados_duzentos_e_setenta_e_sete = Dados(277, date(2023, 5, 19), produto13, 14)
        dados_duzentos_e_setenta_e_oito = Dados(278, date(2023, 5, 19), produto15, 30)
        dados_duzentos_e_setenta_e_nove = Dados(279, date(2023, 5, 20), produto17, 6)
        
        dados_duzentos_e_oitenta = Dados(280, date(2023, 5, 20), produto19, 25)
        dados_duzentos_e_oitenta_e_um = Dados(281, date(2023, 5, 21), produto2, 12)
        dados_duzentos_e_oitenta_e_dois = Dados(282, date(2023, 5, 21), produto4, 18)
        dados_duzentos_e_oitenta_e_tres = Dados(283, date(2023, 5, 22), produto6, 29)
        dados_duzentos_e_oitenta_e_quatro = Dados(284, date(2023, 5, 22), produto8, 9)
        dados_duzentos_e_oitenta_e_cinco = Dados(285, date(2023, 5, 23), produto10, 15)
        dados_duzentos_e_oitenta_e_seis = Dados(286, date(2023, 5, 23), produto12, 20)
        dados_duzentos_e_oitenta_e_sete = Dados(287, date(2023, 5, 24), produto14, 8)
        dados_duzentos_e_oitenta_e_oito = Dados(288, date(2023, 5, 24), produto16, 27)
        dados_duzentos_e_oitenta_e_nove = Dados(289, date(2023, 5, 25), produto18, 13)
        dados_duzentos_e_noventa = Dados(290, date(2023, 5, 25), produto20, 22)
        dados_duzentos_e_noventa_e_um = Dados(291, date(2023, 5, 26), produto1, 18)
        dados_duzentos_e_noventa_e_dois = Dados(292, date(2023, 5, 26), produto3, 6)
        dados_duzentos_e_noventa_e_tres = Dados(293, date(2023, 5, 27), produto5, 28)
        dados_duzentos_e_noventa_e_quatro = Dados(294, date(2023, 5, 27), produto7, 10)
        dados_duzentos_e_noventa_e_cinco = Dados(295, date(2023, 5, 28), produto9, 19)
        dados_duzentos_e_noventa_e_seis = Dados(296, date(2023, 5, 28), produto11, 25)
        dados_duzentos_e_noventa_e_sete = Dados(297, date(2023, 5, 29), produto13, 30)
        dados_duzentos_e_noventa_e_oito = Dados(298, date(2023, 5, 30), produto15, 7)
        dados_duzentos_e_noventa_e_nove = Dados(299, date(2023, 5, 30), produto17, 16)
        dados_trezentos = Dados(300, date(2023, 5, 31), produto19, 23)

        dados_trezentos_e_um = Dados(301, date(2023, 6, 1), produto3, 19)
        dados_trezentos_e_dois = Dados(302, date(2023, 6, 1), produto5, 9)
        dados_trezentos_e_tres = Dados(303, date(2023, 6, 2), produto7, 24)
        dados_trezentos_e_quatro = Dados(304, date(2023, 6, 2), produto9, 15)
        dados_trezentos_e_cinco = Dados(305, date(2023, 6, 3), produto11, 27)
        dados_trezentos_e_seis = Dados(306, date(2023, 6, 3), produto13, 8)
        dados_trezentos_e_sete = Dados(307, date(2023, 6, 4), produto15, 21)
        dados_trezentos_e_oito = Dados(308, date(2023, 6, 4), produto17, 12)
        dados_trezentos_e_nove = Dados(309, date(2023, 6, 5), produto19, 29)
        dados_trezentos_e_dez = Dados(310, date(2023, 6, 5), produto1, 16)
        dados_trezentos_e_onze = Dados(311, date(2023, 6, 6), produto3, 10)
        dados_trezentos_e_doze = Dados(312, date(2023, 6, 6), produto5, 23)
        dados_trezentos_e_treze = Dados(313, date(2023, 6, 7), produto7, 6)
        dados_trezentos_e_quatorze = Dados(314, date(2023, 6, 7), produto9, 18)
        dados_trezentos_e_quinze = Dados(315, date(2023, 6, 8), produto11, 25)
        dados_trezentos_e_dezesseis = Dados(316, date(2023, 6, 8), produto13, 14)
        dados_trezentos_e_dezessete = Dados(317, date(2023, 6, 9), produto15, 28)
        dados_trezentos_e_dezoito = Dados(318, date(2023, 6, 9), produto17, 7)
        dados_trezentos_e_dezenove = Dados(319, date(2023, 6, 10), produto19, 20)

        dados_trezentos_e_vinte = Dados(320, date(2023, 6, 10), produto2, 11)
        dados_trezentos_e_vinte_e_um = Dados(321, date(2023, 6, 11), produto4, 30)
        dados_trezentos_e_vinte_e_dois = Dados(322, date(2023, 6, 11), produto6, 9)
        dados_trezentos_e_vinte_e_tres = Dados(323, date(2023, 6, 12), produto8, 17)
        dados_trezentos_e_vinte_e_quatro = Dados(324, date(2023, 6, 12), produto10, 5)
        dados_trezentos_e_vinte_e_cinco = Dados(325, date(2023, 6, 13), produto12, 22)
        dados_trezentos_e_vinte_e_seis = Dados(326, date(2023, 6, 13), produto14, 13)
        dados_trezentos_e_vinte_e_sete = Dados(327, date(2023, 6, 14), produto16, 27)
        dados_trezentos_e_vinte_e_oito = Dados(328, date(2023, 6, 14), produto18, 6)
        dados_trezentos_e_vinte_e_nove = Dados(329, date(2023, 6, 15), produto20, 19)
        dados_trezentos_e_trinta = Dados(330, date(2023, 6, 15), produto1, 14)
        dados_trezentos_e_trinta_e_um = Dados(331, date(2023, 6, 16), produto3, 8)
        dados_trezentos_e_trinta_e_dois = Dados(332, date(2023, 6, 16), produto5, 25)
        dados_trezentos_e_trinta_e_tres = Dados(333, date(2023, 6, 17), produto7, 18)
        dados_trezentos_e_trinta_e_quatro = Dados(334, date(2023, 6, 17), produto9, 30)
        dados_trezentos_e_trinta_e_cinco = Dados(335, date(2023, 6, 18), produto11, 12)
        dados_trezentos_e_trinta_e_seis = Dados(336, date(2023, 6, 18), produto13, 21)
        dados_trezentos_e_trinta_e_sete = Dados(337, date(2023, 6, 19), produto15, 9)
        dados_trezentos_e_trinta_e_oito = Dados(338, date(2023, 6, 19), produto17, 26)
        dados_trezentos_e_trinta_e_nove = Dados(339, date(2023, 6, 20), produto19, 7)

        dados_trezentos_e_quarenta = Dados(340, date(2023, 6, 20), produto2, 15)
        dados_trezentos_e_quarenta_e_um = Dados(341, date(2023, 6, 21), produto4, 28)
        dados_trezentos_e_quarenta_e_dois = Dados(342, date(2023, 6, 21), produto6, 11)
        dados_trezentos_e_quarenta_e_tres = Dados(343, date(2023, 6, 22), produto8, 24)
        dados_trezentos_e_quarenta_e_quatro = Dados(344, date(2023, 6, 22), produto10, 10)
        dados_trezentos_e_quarenta_e_cinco = Dados(345, date(2023, 6, 23), produto12, 18)
        dados_trezentos_e_quarenta_e_seis = Dados(346, date(2023, 6, 23), produto14, 5)
        dados_trezentos_e_quarenta_e_sete = Dados(347, date(2023, 6, 24), produto16, 22)
        dados_trezentos_e_quarenta_e_oito = Dados(348, date(2023, 6, 24), produto18, 14)
        dados_trezentos_e_quarenta_e_nove = Dados(349, date(2023, 6, 25), produto20, 30)
        dados_trezentos_e_cinquenta = Dados(350, date(2023, 6, 25), produto1, 16)
        dados_trezentos_e_cinquenta_e_um = Dados(351, date(2023, 6, 26), produto3, 20)
        dados_trezentos_e_cinquenta_e_dois = Dados(352, date(2023, 6, 26), produto5, 6)
        dados_trezentos_e_cinquenta_e_tres = Dados(353, date(2023, 6, 27), produto7, 23)
        dados_trezentos_e_cinquenta_e_quatro = Dados(354, date(2023, 6, 27), produto9, 19)
        dados_trezentos_e_cinquenta_e_cinco = Dados(355, date(2023, 6, 28), produto11, 13)
        dados_trezentos_e_cinquenta_e_seis = Dados(356, date(2023, 6, 28), produto13, 29)
        dados_trezentos_e_cinquenta_e_sete = Dados(357, date(2023, 6, 29), produto15, 17)
        dados_trezentos_e_cinquenta_e_oito = Dados(358, date(2023, 6, 29), produto17, 9)
        dados_trezentos_e_cinquenta_e_nove = Dados(359, date(2023, 6, 30), produto19, 26)
        dados_trezentos_e_sessenta = Dados(360, date(2023, 6, 30), produto2, 12)

        dados_trezentos_e_sessenta_e_um = Dados(361, date(2023, 7, 1), produto4, 14)
        dados_trezentos_e_sessenta_e_dois = Dados(362, date(2023, 7, 1), produto6, 27)
        dados_trezentos_e_sessenta_e_tres = Dados(363, date(2023, 7, 2), produto8, 10)
        dados_trezentos_e_sessenta_e_quatro = Dados(364, date(2023, 7, 2), produto10, 22)
        dados_trezentos_e_sessenta_e_cinco = Dados(365, date(2023, 7, 3), produto12, 30)
        dados_trezentos_e_sessenta_e_seis = Dados(366, date(2023, 7, 3), produto14, 18)
        dados_trezentos_e_sessenta_e_sete = Dados(367, date(2023, 7, 4), produto16, 7)
        dados_trezentos_e_sessenta_e_oito = Dados(368, date(2023, 7, 4), produto18, 25)
        dados_trezentos_e_sessenta_e_nove = Dados(369, date(2023, 7, 5), produto20, 13)
        dados_trezentos_e_setenta = Dados(370, date(2023, 7, 5), produto2, 19)
        dados_trezentos_e_setenta_e_um = Dados(371, date(2023, 7, 6), produto4, 21)
        dados_trezentos_e_setenta_e_dois = Dados(372, date(2023, 7, 6), produto6, 9)
        dados_trezentos_e_setenta_e_tres = Dados(373, date(2023, 7, 7), produto8, 28)
        dados_trezentos_e_setenta_e_quatro = Dados(374, date(2023, 7, 7), produto10, 15)
        dados_trezentos_e_setenta_e_cinco = Dados(375, date(2023, 7, 8), produto12, 11)
        dados_trezentos_e_setenta_e_seis = Dados(376, date(2023, 7, 8), produto14, 23)
        dados_trezentos_e_setenta_e_sete = Dados(377, date(2023, 7, 9), produto16, 29)
        dados_trezentos_e_setenta_e_oito = Dados(378, date(2023, 7, 9), produto18, 17)
        dados_trezentos_e_setenta_e_nove = Dados(379, date(2023, 7, 10), produto20, 8)
        
        dados_trezentos_e_oitenta = Dados(380, date(2023, 7, 10), produto2, 26)
        dados_trezentos_e_oitenta_e_um = Dados(381, date(2023, 7, 11), produto4, 20)
        dados_trezentos_e_oitenta_e_dois = Dados(382, date(2023, 7, 11), produto6, 12)
        dados_trezentos_e_oitenta_e_tres = Dados(383, date(2023, 7, 12), produto8, 24)
        dados_trezentos_e_oitenta_e_quatro = Dados(384, date(2023, 7, 12), produto10, 7)
        dados_trezentos_e_oitenta_e_cinco = Dados(385, date(2023, 7, 13), produto12, 18)
        dados_trezentos_e_oitenta_e_seis = Dados(386, date(2023, 7, 13), produto14, 30)
        dados_trezentos_e_oitenta_e_sete = Dados(387, date(2023, 7, 14), produto16, 16)
        dados_trezentos_e_oitenta_e_oito = Dados(388, date(2023, 7, 14), produto18, 5)
        dados_trezentos_e_oitenta_e_nove = Dados(389, date(2023, 7, 15), produto20, 22)
        dados_trezentos_e_noventa = Dados(390, date(2023, 7, 15), produto2, 28)
        dados_trezentos_e_noventa_e_um = Dados(391, date(2023, 7, 16), produto4, 9)
        dados_trezentos_e_noventa_e_dois = Dados(392, date(2023, 7, 16), produto6, 25)
        dados_trezentos_e_noventa_e_tres = Dados(393, date(2023, 7, 17), produto8, 13)
        dados_trezentos_e_noventa_e_quatro = Dados(394, date(2023, 7, 17), produto10, 21)
        dados_trezentos_e_noventa_e_cinco = Dados(395, date(2023, 7, 18), produto12, 15)
        dados_trezentos_e_noventa_e_seis = Dados(396, date(2023, 7, 18), produto14, 10)
        dados_trezentos_e_noventa_e_sete = Dados(397, date(2023, 7, 19), produto16, 27)
        dados_trezentos_e_noventa_e_oito = Dados(398, date(2023, 7, 19), produto18, 19)
        dados_trezentos_e_noventa_e_nove = Dados(399, date(2023, 7, 20), produto20, 30)
        
        dados_quatrocentos = Dados(400, date(2023, 7, 20), produto2, 14)
        dados_quatrocentos_e_um = Dados(401, date(2023, 7, 21), produto4, 11)
        dados_quatrocentos_e_dois = Dados(402, date(2023, 7, 21), produto6, 22)
        dados_quatrocentos_e_tres = Dados(403, date(2023, 7, 22), produto8, 29)
        dados_quatrocentos_e_quatro = Dados(404, date(2023, 7, 22), produto10, 17)
        dados_quatrocentos_e_cinco = Dados(405, date(2023, 7, 23), produto12, 13)
        dados_quatrocentos_e_seis = Dados(406, date(2023, 7, 23), produto14, 26)
        dados_quatrocentos_e_sete = Dados(407, date(2023, 7, 24), produto16, 18)
        dados_quatrocentos_e_oito = Dados(408, date(2023, 7, 24), produto18, 6)
        dados_quatrocentos_e_nove = Dados(409, date(2023, 7, 25), produto20, 23)
        dados_quatrocentos_e_dez = Dados(410, date(2023, 7, 25), produto2, 9)
        dados_quatrocentos_e_onze = Dados(411, date(2023, 7, 26), produto4, 30)
        dados_quatrocentos_e_doze = Dados(412, date(2023, 7, 26), produto6, 15)
        dados_quatrocentos_e_treze = Dados(413, date(2023, 7, 27), produto8, 19)
        dados_quatrocentos_e_quatorze = Dados(414, date(2023, 7, 27), produto10, 8)
        dados_quatrocentos_e_quinze = Dados(415, date(2023, 7, 28), produto12, 21)
        dados_quatrocentos_e_dezesseis = Dados(416, date(2023, 7, 28), produto14, 25)
        dados_quatrocentos_e_dezessete = Dados(417, date(2023, 7, 29), produto16, 12)
        dados_quatrocentos_e_dezoito = Dados(418, date(2023, 7, 29), produto18, 7)
        dados_quatrocentos_e_dezenove = Dados(419, date(2023, 7, 29), produto20, 20)
        dados_quatrocentos_e_vinte = Dados(420, date(2023, 7, 29), produto2, 16)

        dados_quatrocentos_e_vinte_e_um = Dados(421, date(2023, 8, 1), produto3, 18)
        dados_quatrocentos_e_vinte_e_dois = Dados(422, date(2023, 8, 1), produto5, 26)
        dados_quatrocentos_e_vinte_e_tres = Dados(423, date(2023, 8, 2), produto7, 14)
        dados_quatrocentos_e_vinte_e_quatro = Dados(424, date(2023, 8, 2), produto9, 29)
        dados_quatrocentos_e_vinte_e_cinco = Dados(425, date(2023, 8, 3), produto11, 9)
        dados_quatrocentos_e_vinte_e_seis = Dados(426, date(2023, 8, 3), produto13, 23)
        dados_quatrocentos_e_vinte_e_sete = Dados(427, date(2023, 8, 4), produto15, 12)
        dados_quatrocentos_e_vinte_e_oito = Dados(428, date(2023, 8, 4), produto17, 20)
        dados_quatrocentos_e_vinte_e_nove = Dados(429, date(2023, 8, 5), produto19, 7)
        dados_quatrocentos_e_trinta = Dados(430, date(2023, 8, 5), produto1, 27)
        dados_quatrocentos_e_trinta_e_um = Dados(431, date(2023, 8, 6), produto3, 16)
        dados_quatrocentos_e_trinta_e_dois = Dados(432, date(2023, 8, 6), produto5, 21)
        dados_quatrocentos_e_trinta_e_tres = Dados(433, date(2023, 8, 7), produto7, 10)
        dados_quatrocentos_e_trinta_e_quatro = Dados(434, date(2023, 8, 7), produto9, 18)
        dados_quatrocentos_e_trinta_e_cinco = Dados(435, date(2023, 8, 8), produto11, 25)
        dados_quatrocentos_e_trinta_e_seis = Dados(436, date(2023, 8, 8), produto13, 13)
        dados_quatrocentos_e_trinta_e_sete = Dados(437, date(2023, 8, 9), produto15, 30)
        dados_quatrocentos_e_trinta_e_oito = Dados(438, date(2023, 8, 9), produto17, 15)
        dados_quatrocentos_e_trinta_e_nove = Dados(439, date(2023, 8, 10), produto19, 11)
        
        dados_quatrocentos_e_quarenta = Dados(440, date(2023, 8, 10), produto2, 24)
        dados_quatrocentos_e_quarenta_e_um = Dados(441, date(2023, 8, 11), produto4, 19)
        dados_quatrocentos_e_quarenta_e_dois = Dados(442, date(2023, 8, 11), produto6, 27)
        dados_quatrocentos_e_quarenta_e_tres = Dados(443, date(2023, 8, 12), produto8, 8)
        dados_quatrocentos_e_quarenta_e_quatro = Dados(444, date(2023, 8, 12), produto10, 22)
        dados_quatrocentos_e_quarenta_e_cinco = Dados(445, date(2023, 8, 13), produto12, 17)
        dados_quatrocentos_e_quarenta_e_seis = Dados(446, date(2023, 8, 13), produto14, 30)
        dados_quatrocentos_e_quarenta_e_sete = Dados(447, date(2023, 8, 14), produto16, 6)
        dados_quatrocentos_e_quarenta_e_oito = Dados(448, date(2023, 8, 14), produto18, 20)
        dados_quatrocentos_e_quarenta_e_nove = Dados(449, date(2023, 8, 15), produto20, 28)
        dados_quatrocentos_e_cinquenta = Dados(450, date(2023, 8, 15), produto1, 12)
        dados_quatrocentos_e_cinquenta_e_um = Dados(451, date(2023, 8, 16), produto3, 23)
        dados_quatrocentos_e_cinquenta_e_dois = Dados(452, date(2023, 8, 16), produto5, 14)
        dados_quatrocentos_e_cinquenta_e_tres = Dados(453, date(2023, 8, 17), produto7, 26)
        dados_quatrocentos_e_cinquenta_e_quatro = Dados(454, date(2023, 8, 17), produto9, 19)
        dados_quatrocentos_e_cinquenta_e_cinco = Dados(455, date(2023, 8, 18), produto11, 10)
        dados_quatrocentos_e_cinquenta_e_seis = Dados(456, date(2023, 8, 18), produto13, 29)
        dados_quatrocentos_e_cinquenta_e_sete = Dados(457, date(2023, 8, 19), produto15, 16)
        dados_quatrocentos_e_cinquenta_e_oito = Dados(458, date(2023, 8, 19), produto17, 7)
        dados_quatrocentos_e_cinquenta_e_nove = Dados(459, date(2023, 8, 20), produto19, 21)
        
        dados_quatrocentos_e_sessenta = Dados(460, date(2023, 8, 20), produto2, 9)
        dados_quatrocentos_e_sessenta_e_um = Dados(461, date(2023, 8, 21), produto4, 24)
        dados_quatrocentos_e_sessenta_e_dois = Dados(462, date(2023, 8, 21), produto6, 15)
        dados_quatrocentos_e_sessenta_e_tres = Dados(463, date(2023, 8, 22), produto8, 30)
        dados_quatrocentos_e_sessenta_e_quatro = Dados(464, date(2023, 8, 22), produto10, 12)
        dados_quatrocentos_e_sessenta_e_cinco = Dados(465, date(2023, 8, 23), produto12, 27)
        dados_quatrocentos_e_sessenta_e_seis = Dados(466, date(2023, 8, 23), produto14, 18)
        dados_quatrocentos_e_sessenta_e_sete = Dados(467, date(2023, 8, 24), produto16, 5)
        dados_quatrocentos_e_sessenta_e_oito = Dados(468, date(2023, 8, 24), produto18, 25)
        dados_quatrocentos_e_sessenta_e_nove = Dados(469, date(2023, 8, 25), produto20, 13)
        dados_quatrocentos_e_setenta = Dados(470, date(2023, 8, 25), produto1, 19)
        dados_quatrocentos_e_setenta_e_um = Dados(471, date(2023, 8, 26), produto3, 21)
        dados_quatrocentos_e_setenta_e_dois = Dados(472, date(2023, 8, 26), produto5, 7)
        dados_quatrocentos_e_setenta_e_tres = Dados(473, date(2023, 8, 27), produto7, 24)
        dados_quatrocentos_e_setenta_e_quatro = Dados(474, date(2023, 8, 27), produto9, 16)
        dados_quatrocentos_e_setenta_e_cinco = Dados(475, date(2023, 8, 28), produto11, 30)
        dados_quatrocentos_e_setenta_e_seis = Dados(476, date(2023, 8, 28), produto13, 12)
        dados_quatrocentos_e_setenta_e_sete = Dados(477, date(2023, 8, 29), produto15, 18)
        dados_quatrocentos_e_setenta_e_oito = Dados(478, date(2023, 8, 29), produto17, 27)
        dados_quatrocentos_e_setenta_e_nove = Dados(479, date(2023, 8, 30), produto19, 14)
        dados_quatrocentos_e_oitenta = Dados(480, date(2023, 8, 31), produto2, 22)

        dados_quatrocentos_e_oitenta_e_um = Dados(481, date(2023, 9, 1), produto3, 17)
        dados_quatrocentos_e_oitenta_e_dois = Dados(482, date(2023, 9, 1), produto5, 28)
        dados_quatrocentos_e_oitenta_e_tres = Dados(483, date(2023, 9, 2), produto7, 12)
        dados_quatrocentos_e_oitenta_e_quatro = Dados(484, date(2023, 9, 2), produto9, 25)
        dados_quatrocentos_e_oitenta_e_cinco = Dados(485, date(2023, 9, 3), produto11, 10)
        dados_quatrocentos_e_oitenta_e_seis = Dados(486, date(2023, 9, 3), produto13, 22)
        dados_quatrocentos_e_oitenta_e_sete = Dados(487, date(2023, 9, 4), produto15, 14)
        dados_quatrocentos_e_oitenta_e_oito = Dados(488, date(2023, 9, 4), produto17, 30)
        dados_quatrocentos_e_oitenta_e_nove = Dados(489, date(2023, 9, 5), produto19, 8)
        dados_quatrocentos_e_noventa = Dados(490, date(2023, 9, 5), produto1, 27)
        dados_quatrocentos_e_noventa_e_um = Dados(491, date(2023, 9, 6), produto3, 16)
        dados_quatrocentos_e_noventa_e_dois = Dados(492, date(2023, 9, 6), produto5, 21)
        dados_quatrocentos_e_noventa_e_tres = Dados(493, date(2023, 9, 7), produto7, 9)
        dados_quatrocentos_e_noventa_e_quatro = Dados(494, date(2023, 9, 7), produto9, 20)
        dados_quatrocentos_e_noventa_e_cinco = Dados(495, date(2023, 9, 8), produto11, 26)
        dados_quatrocentos_e_noventa_e_seis = Dados(496, date(2023, 9, 8), produto13, 15)
        dados_quatrocentos_e_noventa_e_sete = Dados(497, date(2023, 9, 9), produto15, 19)
        dados_quatrocentos_e_noventa_e_oito = Dados(498, date(2023, 9, 9), produto17, 7)
        dados_quatrocentos_e_noventa_e_nove = Dados(499, date(2023, 9, 10), produto19, 23)
        
        dados_quinhentos = Dados(500, date(2023, 9, 10), produto2, 11)
        dados_quinhentos_e_um = Dados(501, date(2023, 9, 11), produto4, 28)
        dados_quinhentos_e_dois = Dados(502, date(2023, 9, 11), produto6, 14)
        dados_quinhentos_e_tres = Dados(503, date(2023, 9, 12), produto8, 24)
        dados_quinhentos_e_quatro = Dados(504, date(2023, 9, 12), produto10, 9)
        dados_quinhentos_e_cinco = Dados(505, date(2023, 9, 13), produto12, 21)
        dados_quinhentos_e_seis = Dados(506, date(2023, 9, 13), produto14, 18)
        dados_quinhentos_e_sete = Dados(507, date(2023, 9, 14), produto16, 5)
        dados_quinhentos_e_oito = Dados(508, date(2023, 9, 14), produto18, 29)
        dados_quinhentos_e_nove = Dados(509, date(2023, 9, 15), produto20, 13)
        dados_quinhentos_e_dez = Dados(510, date(2023, 9, 15), produto1, 19)
        dados_quinhentos_e_onze = Dados(511, date(2023, 9, 16), produto3, 12)
        dados_quinhentos_e_doze = Dados(512, date(2023, 9, 16), produto5, 25)
        dados_quinhentos_e_treze = Dados(513, date(2023, 9, 17), produto7, 8)
        dados_quinhentos_e_quatorze = Dados(514, date(2023, 9, 17), produto9, 22)
        dados_quinhentos_e_quinze = Dados(515, date(2023, 9, 18), produto11, 27)
        dados_quinhentos_e_dezesseis = Dados(516, date(2023, 9, 18), produto13, 10)
        dados_quinhentos_e_dezessete = Dados(517, date(2023, 9, 19), produto15, 30)
        dados_quinhentos_e_dezoito = Dados(518, date(2023, 9, 19), produto17, 17)
        dados_quinhentos_e_dezenove = Dados(519, date(2023, 9, 20), produto19, 6)
        
        dados_quinhentos_e_vinte = Dados(520, date(2023, 9, 20), produto2, 20)
        dados_quinhentos_e_vinte_e_um = Dados(521, date(2023, 9, 21), produto4, 15)
        dados_quinhentos_e_vinte_e_dois = Dados(522, date(2023, 9, 21), produto6, 29)
        dados_quinhentos_e_vinte_e_tres = Dados(523, date(2023, 9, 22), produto8, 11)
        dados_quinhentos_e_vinte_e_quatro = Dados(524, date(2023, 9, 22), produto10, 24)
        dados_quinhentos_e_vinte_e_cinco = Dados(525, date(2023, 9, 23), produto12, 13)
        dados_quinhentos_e_vinte_e_seis = Dados(526, date(2023, 9, 23), produto14, 26)
        dados_quinhentos_e_vinte_e_sete = Dados(527, date(2023, 9, 24), produto16, 7)
        dados_quinhentos_e_vinte_e_oito = Dados(528, date(2023, 9, 24), produto18, 30)
        dados_quinhentos_e_vinte_e_nove = Dados(529, date(2023, 9, 25), produto20, 18)
        dados_quinhentos_e_trinta = Dados(530, date(2023, 9, 25), produto1, 14)
        dados_quinhentos_e_trinta_e_um = Dados(531, date(2023, 9, 26), produto3, 21)
        dados_quinhentos_e_trinta_e_dois = Dados(532, date(2023, 9, 26), produto5, 16)
        dados_quinhentos_e_trinta_e_tres = Dados(533, date(2023, 9, 27), produto7, 27)
        dados_quinhentos_e_trinta_e_quatro = Dados(534, date(2023, 9, 27), produto9, 12)
        dados_quinhentos_e_trinta_e_cinco = Dados(535, date(2023, 9, 28), produto11, 29)
        dados_quinhentos_e_trinta_e_seis = Dados(536, date(2023, 9, 28), produto13, 8)
        dados_quinhentos_e_trinta_e_sete = Dados(537, date(2023, 9, 29), produto15, 23)
        dados_quinhentos_e_trinta_e_oito = Dados(538, date(2023, 9, 29), produto17, 19)
        dados_quinhentos_e_trinta_e_nove = Dados(539, date(2023, 9, 30), produto19, 11)
        dados_quinhentos_e_quarenta = Dados(540, date(2023, 9, 30), produto2, 24)

        dados_quinhentos_e_quarenta_e_um = Dados(541, date(2023, 10, 1), produto4, 17),
        dados_quinhentos_e_quarenta_e_dois = Dados(542, date(2023, 10, 1), produto6, 25),
        dados_quinhentos_e_quarenta_e_tres = Dados(543, date(2023, 10, 2), produto8, 12),
        dados_quinhentos_e_quarenta_e_quatro = Dados(544, date(2023, 10, 2), produto10, 28),
        dados_quinhentos_e_quarenta_e_cinco = Dados(545, date(2023, 10, 3), produto12, 14),
        dados_quinhentos_e_quarenta_e_seis = Dados(546, date(2023, 10, 3), produto14, 30),
        dados_quinhentos_e_quarenta_e_sete = Dados(547, date(2023, 10, 4), produto16, 9),
        dados_quinhentos_e_quarenta_e_oito = Dados(548, date(2023, 10, 4), produto18, 21),
        dados_quinhentos_e_quarenta_e_nove = Dados(549, date(2023, 10, 5), produto20, 16),
        dados_quinhentos_e_cinquenta = Dados(550, date(2023, 10, 5), produto1, 27),
        dados_quinhentos_e_cinquenta_e_um = Dados(551, date(2023, 10, 6), produto3, 18),
        dados_quinhentos_e_cinquenta_e_dois = Dados(552, date(2023, 10, 6), produto5, 11),
        dados_quinhentos_e_cinquenta_e_tres = Dados(553, date(2023, 10, 7), produto7, 29),
        dados_quinhentos_e_cinquenta_e_quatro = Dados(554, date(2023, 10, 7), produto9, 13),
        dados_quinhentos_e_cinquenta_e_cinco = Dados(555, date(2023, 10, 8), produto11, 22),
        dados_quinhentos_e_cinquenta_e_seis = Dados(556, date(2023, 10, 8), produto13, 7),
        dados_quinhentos_e_cinquenta_e_sete = Dados(557, date(2023, 10, 9), produto15, 26),
        dados_quinhentos_e_cinquenta_e_oito = Dados(558, date(2023, 10, 9), produto17, 15),
        dados_quinhentos_e_cinquenta_e_nove = Dados(559, date(2023, 10, 10), produto19, 20),
      
        dados_quinhentos_e_sessenta = Dados(560, date(2023, 10, 10), produto2, 10),
        dados_quinhentos_e_sessenta_e_um = Dados(561, date(2023, 10, 11), produto4, 23),
        dados_quinhentos_e_sessenta_e_dois = Dados(562, date(2023, 10, 11), produto6, 9),
        dados_quinhentos_e_sessenta_e_tres = Dados(563, date(2023, 10, 12), produto8, 27),
        dados_quinhentos_e_sessenta_e_quatro = Dados(564, date(2023, 10, 12), produto10, 12),
        dados_quinhentos_e_sessenta_e_cinco = Dados(565, date(2023, 10, 13), produto12, 19),
        dados_quinhentos_e_sessenta_e_seis = Dados(566, date(2023, 10, 13), produto14, 16),
        dados_quinhentos_e_sessenta_e_sete = Dados(567, date(2023, 10, 14), produto16, 30),
        dados_quinhentos_e_sessenta_e_oito = Dados(568, date(2023, 10, 14), produto18, 8),
        dados_quinhentos_e_sessenta_e_nove = Dados(569, date(2023, 10, 15), produto20, 25),
        dados_quinhentos_e_setenta = Dados(570, date(2023, 10, 15), produto1, 13),
        dados_quinhentos_e_setenta_e_um = Dados(571, date(2023, 10, 16), produto3, 21),
        dados_quinhentos_e_setenta_e_dois = Dados(572, date(2023, 10, 16), produto5, 17),
        dados_quinhentos_e_setenta_e_tres = Dados(573, date(2023, 10, 17), produto7, 28),
        dados_quinhentos_e_setenta_e_quatro = Dados(574, date(2023, 10, 17), produto9, 15),
        dados_quinhentos_e_setenta_e_cinco = Dados(575, date(2023, 10, 18), produto11, 20),
        dados_quinhentos_e_setenta_e_seis = Dados(576, date(2023, 10, 18), produto13, 10),
        dados_quinhentos_e_setenta_e_sete = Dados(577, date(2023, 10, 19), produto15, 26),
        dados_quinhentos_e_setenta_e_oito = Dados(578, date(2023, 10, 19), produto17, 14),
        dados_quinhentos_e_setenta_e_nove = Dados(579, date(2023, 10, 20), produto19, 12),
      
        dados_quinhentos_e_oitenta = Dados(580, date(2023, 10, 20), produto2, 29),
        dados_quinhentos_e_oitenta_e_um = Dados(581, date(2023, 10, 21), produto4, 18),
        dados_quinhentos_e_oitenta_e_dois = Dados(582, date(2023, 10, 21), produto6, 24),
        dados_quinhentos_e_oitenta_e_tres = Dados(583, date(2023, 10, 22), produto8, 11),
        dados_quinhentos_e_oitenta_e_quatro = Dados(584, date(2023, 10, 22), produto10, 12),
        dados_quinhentos_e_oitenta_e_cinco = Dados(585, date(2023, 10, 23), produto12, 16),
        dados_quinhentos_e_oitenta_e_seis = Dados(586, date(2023, 10, 23), produto14, 30),
        dados_quinhentos_e_oitenta_e_sete = Dados(587, date(2023, 10, 24), produto16, 9),
        dados_quinhentos_e_oitenta_e_oito = Dados(588, date(2023, 10, 24), produto18, 21),
        dados_quinhentos_e_oitenta_e_nove = Dados(589, date(2023, 10, 25), produto20, 19),
        dados_quinhentos_e_noventa = Dados(590, date(2023, 10, 25), produto1, 13),
        dados_quinhentos_e_noventa_e_um = Dados(591, date(2023, 10, 26), produto3, 24),
        dados_quinhentos_e_noventa_e_dois = Dados(592, date(2023, 10, 26), produto5, 15),
        dados_quinhentos_e_noventa_e_tres = Dados(593, date(2023, 10, 27), produto7, 29),
        dados_quinhentos_e_noventa_e_quatro = Dados(594, date(2023, 10, 27), produto9, 12),
        dados_quinhentos_e_noventa_e_cinco = Dados(595, date(2023, 10, 28), produto11, 22),
        dados_quinhentos_e_noventa_e_seis = Dados(596, date(2023, 10, 28), produto13, 10),
        dados_quinhentos_e_noventa_e_sete = Dados(597, date(2023, 10, 29), produto15, 26),
        dados_quinhentos_e_noventa_e_oito = Dados(598, date(2023, 10, 29), produto17, 17),
        dados_quinhentos_e_noventa_e_nove = Dados(599, date(2023, 10, 30), produto14, 14),
        dados_seiscentos = Dados(600, date(2023, 10, 31), produto2, 20)

        dados_seiscentos_e_um = Dados(601, date(2023, 11, 1), produto3, 18),
        dados_seiscentos_e_dois = Dados(602, date(2023, 11, 1), produto5, 27),
        dados_seiscentos_e_tres = Dados(603, date(2023, 11, 2), produto7, 13),
        dados_seiscentos_e_quatro = Dados(604, date(2023, 11, 2), produto9, 22),
        dados_seiscentos_e_cinco = Dados(605, date(2023, 11, 3), produto11, 9),
        dados_seiscentos_e_seis = Dados(606, date(2023, 11, 3), produto13, 25),
        dados_seiscentos_e_sete = Dados(607, date(2023, 11, 4), produto15, 16),
        dados_seiscentos_e_oito = Dados(608, date(2023, 11, 4), produto17, 21),
        dados_seiscentos_e_nove = Dados(609, date(2023, 11, 5), produto19, 10),
        dados_seiscentos_e_dez = Dados(610, date(2023, 11, 5), produto1, 28),
        dados_seiscentos_e_onze = Dados(611, date(2023, 11, 6), produto3, 12),
        dados_seiscentos_e_doze = Dados(612, date(2023, 11, 6), produto5, 20),
        dados_seiscentos_e_treze = Dados(613, date(2023, 11, 7), produto7, 29),
        dados_seiscentos_e_quatorze = Dados(614, date(2023, 11, 7), produto9, 14),
        dados_seiscentos_e_quinze = Dados(615, date(2023, 11, 8), produto11, 17),
        dados_seiscentos_e_dezesseis = Dados(616, date(2023, 11, 8), produto13, 30),
        dados_seiscentos_e_dezessete = Dados(617, date(2023, 11, 9), produto15, 11),
        dados_seiscentos_e_dezoito = Dados(618, date(2023, 11, 9), produto17, 26),
        dados_seiscentos_e_dezenove = Dados(619, date(2023, 11, 10), produto19, 19),
       
        dados_seiscentos_e_vinte = Dados(620, date(2023, 11, 10), produto2, 15),
        dados_seiscentos_e_vinte_e_um = Dados(621, date(2023, 11, 11), produto4, 23),
        dados_seiscentos_e_vinte_e_dois = Dados(622, date(2023, 11, 11), produto6, 12),
        dados_seiscentos_e_vinte_e_tres = Dados(623, date(2023, 11, 12), produto8, 28),
        dados_seiscentos_e_vinte_e_quatro = Dados(624, date(2023, 11, 12), produto10, 9),
        dados_seiscentos_e_vinte_e_cinco = Dados(625, date(2023, 11, 13), produto12, 21),
        dados_seiscentos_e_vinte_e_seis = Dados(626, date(2023, 11, 13), produto8, 16),
        dados_seiscentos_e_vinte_e_sete = Dados(627, date(2023, 11, 14), produto16, 24),
        dados_seiscentos_e_vinte_e_oito = Dados(628, date(2023, 11, 14), produto18, 10),
        dados_seiscentos_e_vinte_e_nove = Dados(629, date(2023, 11, 15), produto20, 27),
        dados_seiscentos_e_trinta = Dados(630, date(2023, 11, 15), produto1, 13),
        dados_seiscentos_e_trinta_e_um = Dados(631, date(2023, 11, 16), produto3, 22),
        dados_seiscentos_e_trinta_e_dois = Dados(632, date(2023, 11, 16), produto5, 15),
        dados_seiscentos_e_trinta_e_tres = Dados(633, date(2023, 11, 17), produto7, 26),
        dados_seiscentos_e_trinta_e_quatro = Dados(634, date(2023, 11, 17), produto9, 18),
        dados_seiscentos_e_trinta_e_cinco = Dados(635, date(2023, 11, 18), produto11, 11),
        dados_seiscentos_e_trinta_e_seis = Dados(636, date(2023, 11, 18), produto13, 29),
        dados_seiscentos_e_trinta_e_sete = Dados(637, date(2023, 11, 19), produto15, 20),
        dados_seiscentos_e_trinta_e_oito = Dados(638, date(2023, 11, 19), produto17, 16),
        dados_seiscentos_e_trinta_e_nove = Dados(639, date(2023, 11, 20), produto19, 12),
       
        dados_seiscentos_e_quarenta = Dados(640, date(2023, 11, 20), produto2, 24),
        dados_seiscentos_e_quarenta_e_um = Dados(641, date(2023, 11, 21), produto9, 17),
        dados_seiscentos_e_quarenta_e_dois = Dados(642, date(2023, 11, 21), produto6, 30),
        dados_seiscentos_e_quarenta_e_tres = Dados(643, date(2023, 11, 22), produto8, 15),
        dados_seiscentos_e_quarenta_e_quatro = Dados(644, date(2023, 11, 22), produto1, 28),
        dados_seiscentos_e_quarenta_e_cinco = Dados(645, date(2023, 11, 23), produto14, 19),
        dados_seiscentos_e_quarenta_e_seis = Dados(646, date(2023, 11, 23), produto3, 10),
        dados_seiscentos_e_quarenta_e_sete = Dados(647, date(2023, 11, 24), produto4, 27),
        dados_seiscentos_e_quarenta_e_oito = Dados(648, date(2023, 11, 24), produto2, 14),
        dados_seiscentos_e_quarenta_e_nove = Dados(649, date(2023, 11, 25), produto20, 11),
        dados_seiscentos_e_cinquenta = Dados(650, date(2023, 11, 25), produto1, 23),
        dados_seiscentos_e_cinquenta_e_um = Dados(651, date(2023, 11, 26), produto3, 16),
        dados_seiscentos_e_cinquenta_e_dois = Dados(652, date(2023, 11, 26), produto5, 30),
        dados_seiscentos_e_cinquenta_e_tres = Dados(653, date(2023, 11, 27), produto7, 13),
        dados_seiscentos_e_cinquenta_e_quatro = Dados(654, date(2023, 11, 27), produto9, 21),
        dados_seiscentos_e_cinquenta_e_cinco = Dados(655, date(2023, 11, 28), produto11, 12),
        dados_seiscentos_e_cinquenta_e_seis = Dados(656, date(2023, 11, 28), produto13, 25),
        dados_seiscentos_e_cinquenta_e_sete = Dados(657, date(2023, 11, 29), produto15, 18),
        dados_seiscentos_e_cinquenta_e_oito = Dados(658, date(2023, 11, 29), produto17, 26),
        dados_seiscentos_e_cinquenta_e_nove = Dados(659, date(2023, 11, 30), produto19, 14),
        dados_seiscentos_e_sessenta = Dados(660, date(2023, 11, 30), produto2, 20)

        dados_seiscentos_e_sessenta_e_um = Dados(661, date(2023, 12, 1), produto3, 19),
        dados_seiscentos_e_sessenta_e_dois = Dados(662, date(2023, 12, 1), produto5, 27),
        dados_seiscentos_e_sessenta_e_tres = Dados(663, date(2023, 12, 2), produto7, 12),
        dados_seiscentos_e_sessenta_e_quatro = Dados(664, date(2023, 12, 2), produto9, 25),
        dados_seiscentos_e_sessenta_e_cinco = Dados(665, date(2023, 12, 3), produto11, 14),
        dados_seiscentos_e_sessenta_e_seis = Dados(666, date(2023, 12, 3), produto13, 30),
        dados_seiscentos_e_sessenta_e_sete = Dados(667, date(2023, 12, 4), produto15, 10),
        dados_seiscentos_e_sessenta_e_oito = Dados(668, date(2023, 12, 4), produto17, 23),
        dados_seiscentos_e_sessenta_e_nove = Dados(669, date(2023, 12, 5), produto19, 16),
        dados_seiscentos_e_setenta = Dados(670, date(2023, 12, 5), produto1, 28),
        dados_seiscentos_e_setenta_e_um = Dados(671, date(2023, 12, 6), produto3, 21),
        dados_seiscentos_e_setenta_e_dois = Dados(672, date(2023, 12, 6), produto5, 13),
        dados_seiscentos_e_setenta_e_tres = Dados(673, date(2023, 12, 7), produto7, 29),
        dados_seiscentos_e_setenta_e_quatro = Dados(674, date(2023, 12, 7), produto9, 15),
        dados_seiscentos_e_setenta_e_cinco = Dados(675, date(2023, 12, 8), produto11, 22),
        dados_seiscentos_e_setenta_e_seis = Dados(676, date(2023, 12, 8), produto13, 11),
        dados_seiscentos_e_setenta_e_sete = Dados(677, date(2023, 12, 9), produto15, 26),
        dados_seiscentos_e_setenta_e_oito = Dados(678, date(2023, 12, 9), produto17, 18),
        dados_seiscentos_e_setenta_e_nove = Dados(679, date(2023, 12, 10), produto19, 20),
        
        dados_seiscentos_e_oitenta = Dados(680, date(2023, 12, 10), produto2, 12),
        dados_seiscentos_e_oitenta_e_um = Dados(681, date(2023, 12, 11), produto4, 24),
        dados_seiscentos_e_oitenta_e_dois = Dados(682, date(2023, 12, 11), produto6, 17),
        dados_seiscentos_e_oitenta_e_tres = Dados(683, date(2023, 12, 12), produto8, 28),
        dados_seiscentos_e_oitenta_e_quatro = Dados(684, date(2023, 12, 12), produto10, 10),
        dados_seiscentos_e_oitenta_e_cinco = Dados(685, date(2023, 12, 13), produto12, 19),
        dados_seiscentos_e_oitenta_e_seis = Dados(686, date(2023, 12, 13), produto14, 15),
        dados_seiscentos_e_oitenta_e_sete = Dados(687, date(2023, 12, 14), produto16, 30),
        dados_seiscentos_e_oitenta_e_oito = Dados(688, date(2023, 12, 14), produto18, 9),
        dados_seiscentos_e_oitenta_e_nove = Dados(689, date(2023, 12, 15), produto20, 26),
        dados_seiscentos_e_noventa = Dados(690, date(2023, 12, 15), produto1, 13),
        dados_seiscentos_e_noventa_e_um = Dados(691, date(2023, 12, 16), produto3, 20),
        dados_seiscentos_e_noventa_e_dois = Dados(692, date(2023, 12, 16), produto5, 14),
        dados_seiscentos_e_noventa_e_tres = Dados(693, date(2023, 12, 17), produto7, 27),
        dados_seiscentos_e_noventa_e_quatro = Dados(694, date(2023, 12, 17), produto9, 11),
        dados_seiscentos_e_noventa_e_cinco = Dados(695, date(2023, 12, 18), produto11, 23),
        dados_seiscentos_e_noventa_e_seis = Dados(696, date(2023, 12, 18), produto13, 12),
        dados_seiscentos_e_noventa_e_sete = Dados(697, date(2023, 12, 19), produto15, 18),
        dados_seiscentos_e_noventa_e_oito = Dados(698, date(2023, 12, 19), produto17, 29),
        dados_seiscentos_e_noventa_e_nove = Dados(699, date(2023, 12, 20), produto19, 15),
        
        dados_setecentos = Dados(700, date(2023, 12, 20), produto2, 21),
        dados_setecentos_e_um = Dados(701, date(2023, 12, 21), produto4, 16),
        dados_setecentos_e_dois = Dados(702, date(2023, 12, 21), produto6, 30),
        dados_setecentos_e_tres = Dados(703, date(2023, 12, 22), produto8, 13),
        dados_setecentos_e_quatro = Dados(704, date(2023, 12, 22), produto10, 25),
        dados_setecentos_e_cinco = Dados(705, date(2023, 12, 23), produto12, 11),
        dados_setecentos_e_seis = Dados(706, date(2023, 12, 23), produto14, 28),
        dados_setecentos_e_sete = Dados(707, date(2023, 12, 24), produto16, 17),
        dados_setecentos_e_oito = Dados(708, date(2023, 12, 24), produto18, 20),
        dados_setecentos_e_nove = Dados(709, date(2023, 12, 25), produto20, 14),
        dados_setecentos_e_dez = Dados(710, date(2023, 12, 25), produto1, 27),
        dados_setecentos_e_onze = Dados(711, date(2023, 12, 26), produto3, 12),
        dados_setecentos_e_doze = Dados(712, date(2023, 12, 26), produto5, 19),
        dados_setecentos_e_treze = Dados(713, date(2023, 12, 27), produto7, 22),
        dados_setecentos_e_quatorze = Dados(714, date(2023, 12, 27), produto9, 15),
        dados_setecentos_e_quinze = Dados(715, date(2023, 12, 28), produto11, 29),
        dados_setecentos_e_dezesseis = Dados(716, date(2023, 12, 28), produto13, 16),
        dados_setecentos_e_dezessete = Dados(717, date(2023, 12, 29), produto15, 18),
        dados_setecentos_e_dezoito = Dados(718, date(2023, 12, 29), produto17, 26),
        dados_setecentos_e_dezenove = Dados(719, date(2023, 12, 30), produto19, 10),
        dados_setecentos_e_vinte = Dados(720, date(2023, 12, 31), produto2, 24)




        dados_janeiro = [dados_um, dados_dois, dados_tres, dados_quatro, dados_cinco, dados_seis, dados_sete, dados_oito, dados_nove, dados_dez, dados_onze, dados_doze, dados_treze, dados_quatorze, dados_quinze, dados_dezesseis, dados_dezessete, dados_dezoito, dados_dezenove, dados_vinte, dados_vinte_um, dados_vinte_dois, dados_vinte_tres, dados_vinte_quatro, dados_vinte_cinco, dados_vinte_seis, dados_vinte_sete, dados_vinte_oito, dados_vinte_nove, dados_trinta, dados_trinta_um, dados_trinta_dois, dados_trinta_tres, dados_trinta_quatro, dados_trinta_cinco, dados_trinta_seis, dados_trinta_sete, dados_trinta_oito, dados_trinta_nove, dados_quarenta, dados_quarenta_um, dados_quarenta_dois, dados_quarenta_tres, dados_quarenta_quatro, dados_quarenta_cinco, dados_quarenta_seis, dados_quarenta_sete, dados_quarenta_oito, dados_quarenta_nove, dados_cinquenta, dados_cinquenta_um, dados_cinquenta_dois, dados_cinquenta_tres, dados_cinquenta_quatro, dados_cinquenta_cinco, dados_cinquenta_seis, dados_cinquenta_sete, dados_cinquenta_oito, dados_cinquenta_nove, dados_sessenta]
        dados_fevereiro = [dados_sessenta_e_um, dados_sessenta_e_dois, dados_sessenta_e_tres, dados_sessenta_e_quatro, dados_sessenta_e_cinco, dados_sessenta_e_seis, dados_sessenta_e_sete, dados_sessenta_e_oito, dados_sessenta_e_nove, dados_setenta, dados_setenta_e_um, dados_setenta_e_dois, dados_setenta_e_tres, dados_setenta_e_quatro, dados_setenta_e_cinco, dados_setenta_e_seis, dados_setenta_e_sete, dados_setenta_e_oito, dados_setenta_e_nove, dados_oitenta, dados_oitenta_e_um, dados_oitenta_e_dois, dados_oitenta_e_tres, dados_oitenta_e_quatro, dados_oitenta_e_cinco, dados_oitenta_e_seis, dados_oitenta_e_sete, dados_oitenta_e_oito, dados_oitenta_e_nove, dados_noventa, dados_noventa_e_um, dados_noventa_e_dois, dados_noventa_e_tres, dados_noventa_e_quatro, dados_noventa_e_cinco, dados_noventa_e_seis, dados_noventa_e_sete, dados_noventa_e_oito, dados_noventa_e_nove, dados_cem, dados_cento_e_um, dados_cento_e_dois, dados_cento_e_tres, dados_cento_e_quatro, dados_cento_e_cinco, dados_cento_e_seis, dados_cento_e_sete, dados_cento_e_oito, dados_cento_e_nove, dados_cento_e_dez, dados_cento_e_onze, dados_cento_e_doze, dados_cento_e_treze, dados_cento_e_quatorze, dados_cento_e_quinze, dados_cento_e_dezesseis, dados_cento_e_dezessete, dados_cento_e_dezoito, dados_cento_e_dezenove, dados_cento_e_vinte]
        dados_marco = [dados_cento_e_vinte_e_um, dados_cento_e_vinte_e_dois, dados_cento_e_vinte_e_tres, dados_cento_e_vinte_e_quatro, dados_cento_e_vinte_e_cinco, dados_cento_e_vinte_e_seis, dados_cento_e_vinte_e_sete, dados_cento_e_vinte_e_oito, dados_cento_e_vinte_e_nove, dados_cento_e_trinta, dados_cento_e_trinta_e_um, dados_cento_e_trinta_e_dois, dados_cento_e_trinta_e_tres, dados_cento_e_trinta_e_quatro, dados_cento_e_trinta_e_cinco, dados_cento_e_trinta_e_seis, dados_cento_e_trinta_e_sete, dados_cento_e_trinta_e_oito, dados_cento_e_trinta_e_nove, dados_cento_e_quarenta, dados_cento_e_quarenta_e_um, dados_cento_e_quarenta_e_dois, dados_cento_e_quarenta_e_tres, dados_cento_e_quarenta_e_quatro, dados_cento_e_quarenta_e_cinco, dados_cento_e_quarenta_e_seis, dados_cento_e_quarenta_e_sete, dados_cento_e_quarenta_e_oito, dados_cento_e_quarenta_e_nove, dados_cento_e_cinquenta, dados_cento_e_cinquenta_e_um, dados_cento_e_cinquenta_e_dois, dados_cento_e_cinquenta_e_tres, dados_cento_e_cinquenta_e_quatro, dados_cento_e_cinquenta_e_cinco, dados_cento_e_cinquenta_e_seis, dados_cento_e_cinquenta_e_sete, dados_cento_e_cinquenta_e_oito, dados_cento_e_cinquenta_e_nove, dados_cento_e_sessenta, dados_cento_e_sessenta_e_um, dados_cento_e_sessenta_e_dois, dados_cento_e_sessenta_e_tres, dados_cento_e_sessenta_e_quatro, dados_cento_e_sessenta_e_cinco, dados_cento_e_sessenta_e_seis, dados_cento_e_sessenta_e_sete, dados_cento_e_sessenta_e_oito, dados_cento_e_sessenta_e_nove, dados_cento_e_setenta, dados_cento_e_setenta_e_um, dados_cento_e_setenta_e_dois, dados_cento_e_setenta_e_tres, dados_cento_e_setenta_e_quatro, dados_cento_e_setenta_e_cinco, dados_cento_e_setenta_e_seis, dados_cento_e_setenta_e_sete, dados_cento_e_setenta_e_oito, dados_cento_e_setenta_e_nove, dados_cento_e_oitenta]
        dados_abril = [dados_cento_e_oitenta_e_um, dados_cento_e_oitenta_e_dois, dados_cento_e_oitenta_e_tres, dados_cento_e_oitenta_e_quatro, dados_cento_e_oitenta_e_cinco, dados_cento_e_oitenta_e_seis, dados_cento_e_oitenta_e_sete, dados_cento_e_oitenta_e_oito, dados_cento_e_oitenta_e_nove, dados_cento_e_noventa, dados_cento_e_noventa_e_um, dados_cento_e_noventa_e_dois, dados_cento_e_noventa_e_tres, dados_cento_e_noventa_e_quatro, dados_cento_e_noventa_e_cinco, dados_cento_e_noventa_e_seis, dados_cento_e_noventa_e_sete, dados_cento_e_noventa_e_oito, dados_cento_e_noventa_e_nove, dados_duzentos, dados_duzentos_e_um, dados_duzentos_e_dois, dados_duzentos_e_tres, dados_duzentos_e_quatro, dados_duzentos_e_cinco, dados_duzentos_e_seis, dados_duzentos_e_sete, dados_duzentos_e_oito, dados_duzentos_e_nove, dados_duzentos_e_dez, dados_duzentos_e_onze, dados_duzentos_e_doze, dados_duzentos_e_treze, dados_duzentos_e_quatorze, dados_duzentos_e_quinze, dados_duzentos_e_dezesseis, dados_duzentos_e_dezessete, dados_duzentos_e_dezoito, dados_duzentos_e_dezenove, dados_duzentos_e_vinte, dados_duzentos_e_vinte_e_um, dados_duzentos_e_vinte_e_dois, dados_duzentos_e_vinte_e_tres, dados_duzentos_e_vinte_e_quatro, dados_duzentos_e_vinte_e_cinco, dados_duzentos_e_vinte_e_seis, dados_duzentos_e_vinte_e_sete, dados_duzentos_e_vinte_e_oito, dados_duzentos_e_vinte_e_nove, dados_duzentos_e_trinta, dados_duzentos_e_trinta_e_um, dados_duzentos_e_trinta_e_dois, dados_duzentos_e_trinta_e_tres, dados_duzentos_e_trinta_e_quatro, dados_duzentos_e_trinta_e_cinco, dados_duzentos_e_trinta_e_seis, dados_duzentos_e_trinta_e_sete, dados_duzentos_e_trinta_e_oito, dados_duzentos_e_trinta_e_nove, dados_duzentos_e_quarenta]
        dados_maio = [dados_duzentos_e_quarenta_e_um, dados_duzentos_e_quarenta_e_dois, dados_duzentos_e_quarenta_e_tres, dados_duzentos_e_quarenta_e_quatro, dados_duzentos_e_quarenta_e_cinco, dados_duzentos_e_quarenta_e_seis, dados_duzentos_e_quarenta_e_sete, dados_duzentos_e_quarenta_e_oito, dados_duzentos_e_quarenta_e_nove, dados_duzentos_e_cinquenta, dados_duzentos_e_cinquenta_e_um, dados_duzentos_e_cinquenta_e_dois, dados_duzentos_e_cinquenta_e_tres, dados_duzentos_e_cinquenta_e_quatro, dados_duzentos_e_cinquenta_e_cinco, dados_duzentos_e_cinquenta_e_seis, dados_duzentos_e_cinquenta_e_sete, dados_duzentos_e_cinquenta_e_oito, dados_duzentos_e_cinquenta_e_nove, dados_duzentos_e_sessenta, dados_duzentos_e_sessenta_e_um, dados_duzentos_e_sessenta_e_dois, dados_duzentos_e_sessenta_e_tres, dados_duzentos_e_sessenta_e_quatro, dados_duzentos_e_sessenta_e_cinco, dados_duzentos_e_sessenta_e_seis, dados_duzentos_e_sessenta_e_sete, dados_duzentos_e_sessenta_e_oito, dados_duzentos_e_sessenta_e_nove, dados_duzentos_e_setenta, dados_duzentos_e_setenta_e_um, dados_duzentos_e_setenta_e_dois, dados_duzentos_e_setenta_e_tres, dados_duzentos_e_setenta_e_quatro, dados_duzentos_e_setenta_e_cinco, dados_duzentos_e_setenta_e_seis, dados_duzentos_e_setenta_e_sete, dados_duzentos_e_setenta_e_oito, dados_duzentos_e_setenta_e_nove, dados_duzentos_e_oitenta, dados_duzentos_e_oitenta_e_um, dados_duzentos_e_oitenta_e_dois, dados_duzentos_e_oitenta_e_tres, dados_duzentos_e_oitenta_e_quatro, dados_duzentos_e_oitenta_e_cinco, dados_duzentos_e_oitenta_e_seis, dados_duzentos_e_oitenta_e_sete, dados_duzentos_e_oitenta_e_oito, dados_duzentos_e_oitenta_e_nove, dados_duzentos_e_noventa, dados_duzentos_e_noventa_e_um, dados_duzentos_e_noventa_e_dois, dados_duzentos_e_noventa_e_tres, dados_duzentos_e_noventa_e_quatro, dados_duzentos_e_noventa_e_cinco, dados_duzentos_e_noventa_e_seis, dados_duzentos_e_noventa_e_sete, dados_duzentos_e_noventa_e_oito, dados_duzentos_e_noventa_e_nove, dados_trezentos]
        dados_junho = [dados_trezentos_e_um, dados_trezentos_e_dois, dados_trezentos_e_tres, dados_trezentos_e_quatro, dados_trezentos_e_cinco, dados_trezentos_e_seis, dados_trezentos_e_sete, dados_trezentos_e_oito, dados_trezentos_e_nove, dados_trezentos_e_dez, dados_trezentos_e_onze, dados_trezentos_e_doze, dados_trezentos_e_treze, dados_trezentos_e_quatorze, dados_trezentos_e_quinze, dados_trezentos_e_dezesseis, dados_trezentos_e_dezessete, dados_trezentos_e_dezoito, dados_trezentos_e_dezenove, dados_trezentos_e_vinte, dados_trezentos_e_vinte_e_um, dados_trezentos_e_vinte_e_dois, dados_trezentos_e_vinte_e_tres, dados_trezentos_e_vinte_e_quatro, dados_trezentos_e_vinte_e_cinco, dados_trezentos_e_vinte_e_seis, dados_trezentos_e_vinte_e_sete, dados_trezentos_e_vinte_e_oito, dados_trezentos_e_vinte_e_nove, dados_trezentos_e_trinta, dados_trezentos_e_trinta_e_um, dados_trezentos_e_trinta_e_dois, dados_trezentos_e_trinta_e_tres, dados_trezentos_e_trinta_e_quatro, dados_trezentos_e_trinta_e_cinco, dados_trezentos_e_trinta_e_seis, dados_trezentos_e_trinta_e_sete, dados_trezentos_e_trinta_e_oito, dados_trezentos_e_trinta_e_nove, dados_trezentos_e_quarenta, dados_trezentos_e_quarenta_e_um, dados_trezentos_e_quarenta_e_dois, dados_trezentos_e_quarenta_e_tres, dados_trezentos_e_quarenta_e_quatro, dados_trezentos_e_quarenta_e_cinco, dados_trezentos_e_quarenta_e_seis, dados_trezentos_e_quarenta_e_sete, dados_trezentos_e_quarenta_e_oito, dados_trezentos_e_quarenta_e_nove, dados_trezentos_e_cinquenta, dados_trezentos_e_cinquenta_e_um, dados_trezentos_e_cinquenta_e_dois, dados_trezentos_e_cinquenta_e_tres, dados_trezentos_e_cinquenta_e_quatro, dados_trezentos_e_cinquenta_e_cinco, dados_trezentos_e_cinquenta_e_seis, dados_trezentos_e_cinquenta_e_sete, dados_trezentos_e_cinquenta_e_oito, dados_trezentos_e_cinquenta_e_nove, dados_trezentos_e_sessenta]
        dados_julho = [dados_trezentos_e_sessenta_e_um, dados_trezentos_e_sessenta_e_dois, dados_trezentos_e_sessenta_e_tres, dados_trezentos_e_sessenta_e_quatro, dados_trezentos_e_sessenta_e_cinco, dados_trezentos_e_sessenta_e_seis, dados_trezentos_e_sessenta_e_sete, dados_trezentos_e_sessenta_e_oito, dados_trezentos_e_sessenta_e_nove, dados_trezentos_e_setenta, dados_trezentos_e_setenta_e_um, dados_trezentos_e_setenta_e_dois, dados_trezentos_e_setenta_e_tres, dados_trezentos_e_setenta_e_quatro, dados_trezentos_e_setenta_e_cinco, dados_trezentos_e_setenta_e_seis, dados_trezentos_e_setenta_e_sete, dados_trezentos_e_setenta_e_oito, dados_trezentos_e_setenta_e_nove, dados_trezentos_e_oitenta, dados_trezentos_e_oitenta_e_um, dados_trezentos_e_oitenta_e_dois, dados_trezentos_e_oitenta_e_tres, dados_trezentos_e_oitenta_e_quatro, dados_trezentos_e_oitenta_e_cinco, dados_trezentos_e_oitenta_e_seis, dados_trezentos_e_oitenta_e_sete, dados_trezentos_e_oitenta_e_oito, dados_trezentos_e_oitenta_e_nove, dados_trezentos_e_noventa, dados_trezentos_e_noventa_e_um, dados_trezentos_e_noventa_e_dois, dados_trezentos_e_noventa_e_tres, dados_trezentos_e_noventa_e_quatro, dados_trezentos_e_noventa_e_cinco, dados_trezentos_e_noventa_e_seis, dados_trezentos_e_noventa_e_sete, dados_trezentos_e_noventa_e_oito, dados_trezentos_e_noventa_e_nove, dados_quatrocentos, dados_quatrocentos_e_um, dados_quatrocentos_e_dois, dados_quatrocentos_e_tres, dados_quatrocentos_e_quatro, dados_quatrocentos_e_cinco, dados_quatrocentos_e_seis, dados_quatrocentos_e_sete, dados_quatrocentos_e_oito, dados_quatrocentos_e_nove, dados_quatrocentos_e_dez, dados_quatrocentos_e_onze, dados_quatrocentos_e_doze, dados_quatrocentos_e_treze, dados_quatrocentos_e_quatorze, dados_quatrocentos_e_quinze, dados_quatrocentos_e_dezesseis, dados_quatrocentos_e_dezessete, dados_quatrocentos_e_dezoito, dados_quatrocentos_e_dezenove, dados_quatrocentos_e_vinte]
        dados_agosto = [dados_quatrocentos_e_vinte_e_um, dados_quatrocentos_e_vinte_e_dois, dados_quatrocentos_e_vinte_e_tres, dados_quatrocentos_e_vinte_e_quatro, dados_quatrocentos_e_vinte_e_cinco, dados_quatrocentos_e_vinte_e_seis, dados_quatrocentos_e_vinte_e_sete, dados_quatrocentos_e_vinte_e_oito, dados_quatrocentos_e_vinte_e_nove, dados_quatrocentos_e_trinta, dados_quatrocentos_e_trinta_e_um, dados_quatrocentos_e_trinta_e_dois, dados_quatrocentos_e_trinta_e_tres, dados_quatrocentos_e_trinta_e_quatro, dados_quatrocentos_e_trinta_e_cinco, dados_quatrocentos_e_trinta_e_seis, dados_quatrocentos_e_trinta_e_sete, dados_quatrocentos_e_trinta_e_oito, dados_quatrocentos_e_trinta_e_nove, dados_quatrocentos_e_quarenta, dados_quatrocentos_e_quarenta_e_um, dados_quatrocentos_e_quarenta_e_dois, dados_quatrocentos_e_quarenta_e_tres, dados_quatrocentos_e_quarenta_e_quatro, dados_quatrocentos_e_quarenta_e_cinco, dados_quatrocentos_e_quarenta_e_seis, dados_quatrocentos_e_quarenta_e_sete, dados_quatrocentos_e_quarenta_e_oito, dados_quatrocentos_e_quarenta_e_nove, dados_quatrocentos_e_cinquenta, dados_quatrocentos_e_cinquenta_e_um, dados_quatrocentos_e_cinquenta_e_dois, dados_quatrocentos_e_cinquenta_e_tres, dados_quatrocentos_e_cinquenta_e_quatro, dados_quatrocentos_e_cinquenta_e_cinco, dados_quatrocentos_e_cinquenta_e_seis, dados_quatrocentos_e_cinquenta_e_sete, dados_quatrocentos_e_cinquenta_e_oito, dados_quatrocentos_e_cinquenta_e_nove, dados_quatrocentos_e_sessenta, dados_quatrocentos_e_sessenta_e_um, dados_quatrocentos_e_sessenta_e_dois, dados_quatrocentos_e_sessenta_e_tres, dados_quatrocentos_e_sessenta_e_quatro, dados_quatrocentos_e_sessenta_e_cinco, dados_quatrocentos_e_sessenta_e_seis, dados_quatrocentos_e_sessenta_e_sete, dados_quatrocentos_e_sessenta_e_oito, dados_quatrocentos_e_sessenta_e_nove, dados_quatrocentos_e_setenta, dados_quatrocentos_e_setenta_e_um, dados_quatrocentos_e_setenta_e_dois, dados_quatrocentos_e_setenta_e_tres, dados_quatrocentos_e_setenta_e_quatro, dados_quatrocentos_e_setenta_e_cinco, dados_quatrocentos_e_setenta_e_seis, dados_quatrocentos_e_setenta_e_sete, dados_quatrocentos_e_setenta_e_oito, dados_quatrocentos_e_setenta_e_nove, dados_quatrocentos_e_oitenta]
        dados_setembro = [dados_quatrocentos_e_oitenta_e_um, dados_quatrocentos_e_oitenta_e_dois, dados_quatrocentos_e_oitenta_e_tres, dados_quatrocentos_e_oitenta_e_quatro, dados_quatrocentos_e_oitenta_e_cinco, dados_quatrocentos_e_oitenta_e_seis, dados_quatrocentos_e_oitenta_e_sete, dados_quatrocentos_e_oitenta_e_oito, dados_quatrocentos_e_oitenta_e_nove, dados_quatrocentos_e_noventa, dados_quatrocentos_e_noventa_e_um, dados_quatrocentos_e_noventa_e_dois, dados_quatrocentos_e_noventa_e_tres, dados_quatrocentos_e_noventa_e_quatro, dados_quatrocentos_e_noventa_e_cinco, dados_quatrocentos_e_noventa_e_seis, dados_quatrocentos_e_noventa_e_sete, dados_quatrocentos_e_noventa_e_oito, dados_quatrocentos_e_noventa_e_nove, dados_quinhentos, dados_quinhentos_e_um, dados_quinhentos_e_dois, dados_quinhentos_e_tres, dados_quinhentos_e_quatro, dados_quinhentos_e_cinco, dados_quinhentos_e_seis, dados_quinhentos_e_sete, dados_quinhentos_e_oito, dados_quinhentos_e_nove, dados_quinhentos_e_dez, dados_quinhentos_e_onze, dados_quinhentos_e_doze, dados_quinhentos_e_treze, dados_quinhentos_e_quatorze, dados_quinhentos_e_quinze, dados_quinhentos_e_dezesseis, dados_quinhentos_e_dezessete, dados_quinhentos_e_dezoito, dados_quinhentos_e_dezenove, dados_quinhentos_e_vinte, dados_quinhentos_e_vinte_e_um, dados_quinhentos_e_vinte_e_dois, dados_quinhentos_e_vinte_e_tres, dados_quinhentos_e_vinte_e_quatro, dados_quinhentos_e_vinte_e_cinco, dados_quinhentos_e_vinte_e_seis, dados_quinhentos_e_vinte_e_sete, dados_quinhentos_e_vinte_e_oito, dados_quinhentos_e_vinte_e_nove, dados_quinhentos_e_trinta, dados_quinhentos_e_trinta_e_um, dados_quinhentos_e_trinta_e_dois, dados_quinhentos_e_trinta_e_tres, dados_quinhentos_e_trinta_e_quatro, dados_quinhentos_e_trinta_e_cinco, dados_quinhentos_e_trinta_e_seis, dados_quinhentos_e_trinta_e_sete, dados_quinhentos_e_trinta_e_oito, dados_quinhentos_e_trinta_e_nove, dados_quinhentos_e_quarenta]
        dados_outubro = [dados_quinhentos_e_quarenta_e_um, dados_quinhentos_e_quarenta_e_dois, dados_quinhentos_e_quarenta_e_tres, dados_quinhentos_e_quarenta_e_quatro, dados_quinhentos_e_quarenta_e_cinco, dados_quinhentos_e_quarenta_e_seis, dados_quinhentos_e_quarenta_e_sete, dados_quinhentos_e_quarenta_e_oito, dados_quinhentos_e_quarenta_e_nove, dados_quinhentos_e_cinquenta, dados_quinhentos_e_cinquenta_e_um, dados_quinhentos_e_cinquenta_e_dois, dados_quinhentos_e_cinquenta_e_tres, dados_quinhentos_e_cinquenta_e_quatro, dados_quinhentos_e_cinquenta_e_cinco, dados_quinhentos_e_cinquenta_e_seis, dados_quinhentos_e_cinquenta_e_sete, dados_quinhentos_e_cinquenta_e_oito, dados_quinhentos_e_cinquenta_e_nove, dados_quinhentos_e_sessenta, dados_quinhentos_e_sessenta_e_um, dados_quinhentos_e_sessenta_e_dois, dados_quinhentos_e_sessenta_e_tres, dados_quinhentos_e_sessenta_e_quatro, dados_quinhentos_e_sessenta_e_cinco, dados_quinhentos_e_sessenta_e_seis, dados_quinhentos_e_sessenta_e_sete, dados_quinhentos_e_sessenta_e_oito, dados_quinhentos_e_sessenta_e_nove, dados_quinhentos_e_setenta, dados_quinhentos_e_setenta_e_um, dados_quinhentos_e_setenta_e_dois, dados_quinhentos_e_setenta_e_tres, dados_quinhentos_e_setenta_e_quatro, dados_quinhentos_e_setenta_e_cinco, dados_quinhentos_e_setenta_e_seis, dados_quinhentos_e_setenta_e_sete, dados_quinhentos_e_setenta_e_oito, dados_quinhentos_e_setenta_e_nove, dados_quinhentos_e_oitenta, dados_quinhentos_e_oitenta_e_um, dados_quinhentos_e_oitenta_e_dois, dados_quinhentos_e_oitenta_e_tres, dados_quinhentos_e_oitenta_e_quatro, dados_quinhentos_e_oitenta_e_cinco, dados_quinhentos_e_oitenta_e_seis, dados_quinhentos_e_oitenta_e_sete, dados_quinhentos_e_oitenta_e_oito, dados_quinhentos_e_oitenta_e_nove, dados_quinhentos_e_noventa, dados_quinhentos_e_noventa_e_um, dados_quinhentos_e_noventa_e_dois, dados_quinhentos_e_noventa_e_tres, dados_quinhentos_e_noventa_e_quatro, dados_quinhentos_e_noventa_e_cinco, dados_quinhentos_e_noventa_e_seis, dados_quinhentos_e_noventa_e_sete, dados_quinhentos_e_noventa_e_oito, dados_quinhentos_e_noventa_e_nove, dados_seiscentos]
        dados_novembro = [dados_seiscentos_e_um, dados_seiscentos_e_dois, dados_seiscentos_e_tres, dados_seiscentos_e_quatro, dados_seiscentos_e_cinco, dados_seiscentos_e_seis, dados_seiscentos_e_sete, dados_seiscentos_e_oito, dados_seiscentos_e_nove, dados_seiscentos_e_dez, dados_seiscentos_e_onze, dados_seiscentos_e_doze, dados_seiscentos_e_treze, dados_seiscentos_e_quatorze, dados_seiscentos_e_quinze, dados_seiscentos_e_dezesseis, dados_seiscentos_e_dezessete, dados_seiscentos_e_dezoito, dados_seiscentos_e_dezenove, dados_seiscentos_e_vinte, dados_seiscentos_e_vinte_e_um, dados_seiscentos_e_vinte_e_dois, dados_seiscentos_e_vinte_e_tres, dados_seiscentos_e_vinte_e_quatro, dados_seiscentos_e_vinte_e_cinco, dados_seiscentos_e_vinte_e_seis, dados_seiscentos_e_vinte_e_sete, dados_seiscentos_e_vinte_e_oito, dados_seiscentos_e_vinte_e_nove, dados_seiscentos_e_trinta, dados_seiscentos_e_trinta_e_um, dados_seiscentos_e_trinta_e_dois, dados_seiscentos_e_trinta_e_tres, dados_seiscentos_e_trinta_e_quatro, dados_seiscentos_e_trinta_e_cinco, dados_seiscentos_e_trinta_e_seis, dados_seiscentos_e_trinta_e_sete, dados_seiscentos_e_trinta_e_oito, dados_seiscentos_e_trinta_e_nove, dados_seiscentos_e_quarenta, dados_seiscentos_e_quarenta_e_um, dados_seiscentos_e_quarenta_e_dois, dados_seiscentos_e_quarenta_e_tres, dados_seiscentos_e_quarenta_e_quatro, dados_seiscentos_e_quarenta_e_cinco, dados_seiscentos_e_quarenta_e_seis, dados_seiscentos_e_quarenta_e_sete, dados_seiscentos_e_quarenta_e_oito, dados_seiscentos_e_quarenta_e_nove, dados_seiscentos_e_cinquenta, dados_seiscentos_e_cinquenta_e_um, dados_seiscentos_e_cinquenta_e_dois, dados_seiscentos_e_cinquenta_e_tres, dados_seiscentos_e_cinquenta_e_quatro, dados_seiscentos_e_cinquenta_e_cinco, dados_seiscentos_e_cinquenta_e_seis, dados_seiscentos_e_cinquenta_e_sete, dados_seiscentos_e_cinquenta_e_oito, dados_seiscentos_e_cinquenta_e_nove, dados_seiscentos_e_sessenta]
        dados_dezembro = [dados_seiscentos_e_sessenta_e_um, dados_seiscentos_e_sessenta_e_dois, dados_seiscentos_e_sessenta_e_tres, dados_seiscentos_e_sessenta_e_quatro, dados_seiscentos_e_sessenta_e_cinco, dados_seiscentos_e_sessenta_e_seis, dados_seiscentos_e_sessenta_e_sete, dados_seiscentos_e_sessenta_e_oito, dados_seiscentos_e_sessenta_e_nove, dados_seiscentos_e_setenta, dados_seiscentos_e_setenta_e_um, dados_seiscentos_e_setenta_e_dois, dados_seiscentos_e_setenta_e_tres, dados_seiscentos_e_setenta_e_quatro, dados_seiscentos_e_setenta_e_cinco, dados_seiscentos_e_setenta_e_seis, dados_seiscentos_e_setenta_e_sete, dados_seiscentos_e_setenta_e_oito, dados_seiscentos_e_setenta_e_nove, dados_seiscentos_e_oitenta, dados_seiscentos_e_oitenta_e_um, dados_seiscentos_e_oitenta_e_dois, dados_seiscentos_e_oitenta_e_tres, dados_seiscentos_e_oitenta_e_quatro, dados_seiscentos_e_oitenta_e_cinco, dados_seiscentos_e_oitenta_e_seis, dados_seiscentos_e_oitenta_e_sete, dados_seiscentos_e_oitenta_e_oito, dados_seiscentos_e_oitenta_e_nove, dados_seiscentos_e_noventa, dados_seiscentos_e_noventa_e_um, dados_seiscentos_e_noventa_e_dois, dados_seiscentos_e_noventa_e_tres, dados_seiscentos_e_noventa_e_quatro, dados_seiscentos_e_noventa_e_cinco, dados_seiscentos_e_noventa_e_seis, dados_seiscentos_e_noventa_e_sete, dados_seiscentos_e_noventa_e_oito, dados_seiscentos_e_noventa_e_nove, dados_setecentos, dados_setecentos_e_um, dados_setecentos_e_dois, dados_setecentos_e_tres, dados_setecentos_e_quatro, dados_setecentos_e_cinco, dados_setecentos_e_seis, dados_setecentos_e_sete, dados_setecentos_e_oito, dados_setecentos_e_nove, dados_setecentos_e_dez, dados_setecentos_e_onze, dados_setecentos_e_doze, dados_setecentos_e_treze, dados_setecentos_e_quatorze, dados_setecentos_e_quinze, dados_setecentos_e_dezesseis, dados_setecentos_e_dezessete, dados_setecentos_e_dezoito, dados_setecentos_e_dezenove, dados_setecentos_e_vinte]

        return [dados_janeiro, dados_fevereiro, dados_marco, dados_abril, dados_maio, dados_junho, dados_julho, dados_agosto, dados_setembro,
                dados_outubro, dados_novembro, dados_dezembro]


    def formatar_numero(self, num):

        num_em_str = str(num)

        num_cortado = num_em_str.split('.')
        numero_para_concatenar = num_cortado[0]
        numero_decimal_para_formatar = num_cortado[1]
        decimal = num_cortado[1]

        contador = 0
        lista_do_decimal = []
        while (contador <= 1):
            lista_do_decimal.append(decimal[contador])
            contador += 1

        num_final_str = numero_para_concatenar +'.'+lista_do_decimal[0] + lista_do_decimal[1]
        num_final = float(num_final_str)
        return num_final

    def montar_data_set(self):
        lista_base = self.montar_dados()

        """
        essa é uma forma de segurança para garantia de que se tiver alguma informação faltante 
        vou conseguir buscar em outra fonte.
        """
        produto1 = Produto(1, "", "Medicamentos", 7.5000)
        produto2 = Produto(2, "Dipirona 500mg", "Medicamentos", 5.9090)
        produto3 = Produto(3, "Ibuprofeno 400mg", "Medicamentos", 8.9098)
        produto4 = Produto(4, "Sabonete Lux", "Produtos de higiene pessoal", 3.5013)
        produto5 = Produto(5, "Shampoo Seda", "Produtos de higiene pessoal", 9.9543)
        produto6 = Produto(6, "Creme Dental Colgate", "Produtos de higiene pessoal", 6.95098)
        produto7 = Produto(7, "Batom Maybelline", "Produtos de beleza", 29.9012)
        produto8 = Produto(8, "Base Vult", "Produtos de beleza", 35.9032)
        produto9 = Produto(9, "Perfume Natura", "Não consta", 89.993232)
        produto10 = Produto(10, "Multivitamínico Centrum", "Produtos de bem-estar", 29.9099)
        produto11 = Produto(11, "Ômega 3 Sundown", "Produtos de bem-estar", 49.90332)
        produto12 = Produto(12, "Chá de Camomila", "Produtos de bem-estar", 4.9012)
        produto13 = Produto(13, "Fralda Pampers Confort Sec G", "Produtos para bebês", 189.9032)
        produto14 = Produto(14, "Lenço Umedecido Huggies", "Produtos para bebês", 9.90323)
        produto15 = Produto(15, "Fórmula Infantil Nan", "Produtos para bebês", 39.90323)
        produto16 = Produto(16, "Gaze Estéril", "Produtos hospitalares e de primeiros socorros", 6.90213)
        produto17 = Produto(17, "Álcool 70%", "Produtos hospitalares e de primeiros socorros", 3.903232)
        produto18 = Produto(18, "Termômetro Digital", "Produtos hospitalares e de primeiros socorros", 45.9032)
        produto19 = Produto(19, "Chocolate Snickers", "Produtos de conveniência", 5.49233)
        produto20 = Produto(20, "Biscoito Oreo", "Produtos de conveniência", 6.90323)
        produto21 = Produto(21, "Suco de Laranja Del Valle", "Produtos de conveniência", 4.90323)

        lista_de_emergencia_produtos = [produto1, produto2, produto3, produto4, produto5, produto6, produto7,
                                        produto8, produto9, produto10, produto11, produto12, produto13, produto14, produto15,
                                        produto16, produto17, produto18, produto19, produto20, produto21]

        dados_janeiro = lista_base[0]
        dados_fevereiro = lista_base[1]
        dados_marco = lista_base[2]
        dados_abril = lista_base[3]
        dados_maio = lista_base[4]
        dados_junho = lista_base[5]
        dados_julho = lista_base[6]
        dados_agosto = lista_base[7]
        dados_setembro = lista_base[8]
        dados_outubro = lista_base[9]
        dados_novembro = lista_base[10]
        dados_dezembro = lista_base[11]


        dataset_vendas_meses = {"janeiro" : dados_janeiro, "fevereiro" : dados_fevereiro,
                    "marco" : dados_marco, "abril" : dados_abril, "maio" : dados_maio,
                    "junho" : dados_junho,  "julho" : dados_julho, "agosto" : dados_agosto, 
                    "setembro" : dados_setembro, "outubro" : dados_outubro, 
                    "novembro" : dados_novembro, "dezembro" : dados_dezembro}
        
        dados_janeiro_tratados = []
        dados_fevereiro_tratados = []
        dados_marco_tratados = []
        dados_abril_tratados = []
        dados_maio_tratados = []
        dados_junho_tratados = []
        dados_julho_tratados = []
        dados_agosto_tratados = []
        dados_setembro_tratados = []
        dados_outubro_tratados = []
        dados_novembro_tratados = []
        dados_dezembro_tratados = []

        contador = 0
        while(contador < 720):
            if contador >= 0 and contador <= 59:
                if(dataset_vendas_meses["janeiro"][contador].produto.nome == "" or dataset_vendas_meses["janeiro"][contador].produto.nome == " "):
                    for item in lista_de_emergencia_produtos:
                        if dataset_vendas_meses["janeiro"][contador].produto.id == item.id:
                            dataset_vendas_meses["janeiro"][contador].produto.nome = item.nome
                            break

                if(dataset_vendas_meses["janeiro"][contador].produto.categoria == "" or dataset_vendas_meses["janeiro"][contador].produto.categoria == " "):
                    for item in lista_de_emergencia_produtos:
                        if dataset_vendas_meses["janeiro"][contador].produto.id == item.id:
                            dataset_vendas_meses["janeiro"][contador].produto.categoria = item.categoria
                            break

                if (dataset_vendas_meses["janeiro"][contador].produto.preco == 0):

                    for item in lista_de_emergencia_produtos:
                        if dataset_vendas_meses["janeiro"][contador].produto.id == item.id:
                            self.formatar_numero(item.preco)
                            dataset_vendas_meses["janeiro"][contador].produto.preco = item.preco
                            break

                precoDefinitivo = self.formatar_numero(dataset_vendas_meses["janeiro"][contador].produto.preco)
                dataset_vendas_meses["janeiro"][contador].produto.preco = precoDefinitivo
                dados_janeiro_tratados.append(dataset_vendas_meses["janeiro"][contador])

            if contador >= 60 and contador <= 119:
                if(dataset_vendas_meses["fevereiro"][contador].produto.nome == "" or dataset_vendas_meses["fevereiro"][contador].produto.nome == " "):
                    for item in lista_de_emergencia_produtos:
                        if dataset_vendas_meses["fevereiro"][contador].produto.id == item.id:
                            dataset_vendas_meses["fevereiro"][contador].produto.nome = item.nome
                            break

                if(dataset_vendas_meses["fevereiro"][contador].produto.categoria == "" or dataset_vendas_meses["fevereiro"][contador].produto.categoria == " "):
                    for item in lista_de_emergencia_produtos:
                        if dataset_vendas_meses["fevereiro"][contador].produto.id == item.id:
                            dataset_vendas_meses["fevereiro"][contador].produto.categoria = item.categoria
                            break

                if (dataset_vendas_meses["fevereiro"][contador].produto.preco == 0):

                    for item in lista_de_emergencia_produtos:
                        if dataset_vendas_meses["fevereiro"][contador].produto.id == item.id:
                            self.formatar_numero(item.preco)
                            dataset_vendas_meses["fevereiro"][contador].produto.preco = item.preco

                            break

                precoDefinitivo = self.formatar_numero(dataset_vendas_meses["fevereiro"][contador].produto.preco)
                dataset_vendas_meses["fevereiro"][contador].produto.preco = precoDefinitivo
                dados_fevereiro_tratados.append(dataset_vendas_meses["fevereiro"][contador])

            if contador >= 120 and contador <= 179:
                if(dataset_vendas_meses["marco"][contador].produto.nome == "" or dataset_vendas_meses["marco"][contador].produto.nome == " "):
                    for item in lista_de_emergencia_produtos:
                        if dataset_vendas_meses["marco"][contador].produto.id == item.id:
                            dataset_vendas_meses["marco"][contador].produto.nome = item.nome
                            break

                if(dataset_vendas_meses["marco"][contador].produto.categoria == "" or dataset_vendas_meses["marco"][contador].produto.categoria == " "):
                    for item in lista_de_emergencia_produtos:
                        if dataset_vendas_meses["marco"][contador].produto.id == item.id:
                            dataset_vendas_meses["marco"][contador].produto.categoria = item.categoria
                            break

                if (dataset_vendas_meses["marco"][contador].produto.preco == 0):

                    for item in lista_de_emergencia_produtos:
                        if dataset_vendas_meses["marco"][contador].produto.id == item.id:
                            self.formatar_numero(item.preco)
                            dataset_vendas_meses["marco"][contador].produto.preco = item.preco

                            break

                precoDefinitivo = self.formatar_numero(dataset_vendas_meses["marco"][contador].produto.preco)
                dataset_vendas_meses["marco"][contador].produto.preco = precoDefinitivo
                dados_marco_tratados.append(dataset_vendas_meses["marco"][contador])

            if contador >= 180 and contador <= 239:
                if(dataset_vendas_meses["abril"][contador].produto.nome == "" or dataset_vendas_meses["abril"][contador].produto.nome == " "):
                    for item in lista_de_emergencia_produtos:
                        if dataset_vendas_meses["abril"][contador].produto.id == item.id:
                            dataset_vendas_meses["abril"][contador].produto.nome = item.nome
                            break

                if(dataset_vendas_meses["abril"][contador].produto.categoria == "" or dataset_vendas_meses["abril"][contador].produto.categoria == " "):
                    for item in lista_de_emergencia_produtos:
                        if dataset_vendas_meses["abril"][contador].produto.id == item.id:
                            dataset_vendas_meses["abril"][contador].produto.categoria = item.categoria
                            break

                if (dataset_vendas_meses["abril"][contador].produto.preco == 0):

                    for item in lista_de_emergencia_produtos:
                        if dataset_vendas_meses["abril"][contador].produto.id == item.id:
                            self.formatar_numero(item.preco)
                            dataset_vendas_meses["abril"][contador].produto.preco = item.preco

                            break

                precoDefinitivo = self.formatar_numero(dataset_vendas_meses["abril"][contador].produto.preco)
                dataset_vendas_meses["abril"][contador].produto.preco = precoDefinitivo
                dados_abril_tratados.append(dataset_vendas_meses["abril"][contador])

            if contador >= 240 and contador <= 299:
                if(dataset_vendas_meses["maio"][contador].produto.nome == "" or dataset_vendas_meses["maio"][contador].produto.nome == " "):
                    for item in lista_de_emergencia_produtos:
                        if dataset_vendas_meses["maio"][contador].produto.id == item.id:
                            dataset_vendas_meses["maio"][contador].produto.nome = item.nome
                            break

                if(dataset_vendas_meses["maio"][contador].produto.categoria == "" or dataset_vendas_meses["maio"][contador].produto.categoria == " "):
                    for item in lista_de_emergencia_produtos:
                        if dataset_vendas_meses["maio"][contador].produto.id == item.id:
                            dataset_vendas_meses["maio"][contador].produto.categoria = item.categoria
                            break

                if (dataset_vendas_meses["maio"][contador].produto.preco == 0):

                    for item in lista_de_emergencia_produtos:
                        if dataset_vendas_meses["maio"][contador].produto.id == item.id:
                            self.formatar_numero(item.preco)
                            dataset_vendas_meses["maio"][contador].produto.preco = item.preco

                            break

                precoDefinitivo = self.formatar_numero(dataset_vendas_meses["maio"][contador].produto.preco)
                dataset_vendas_meses["maio"][contador].produto.preco = precoDefinitivo
                dados_maio_tratados.append(dataset_vendas_meses["maio"][contador])

            if contador >= 300 and contador <= 359:
                if(dataset_vendas_meses["junho"][contador].produto.nome == "" or dataset_vendas_meses["junho"][contador].produto.nome == " "):
                    for item in lista_de_emergencia_produtos:
                        if dataset_vendas_meses["junho"][contador].produto.id == item.id:
                            dataset_vendas_meses["junho"][contador].produto.nome = item.nome
                            break

                if(dataset_vendas_meses["junho"][contador].produto.categoria == "" or dataset_vendas_meses["junho"][contador].produto.categoria == " "):
                    for item in lista_de_emergencia_produtos:
                        if dataset_vendas_meses["junho"][contador].produto.id == item.id:
                            dataset_vendas_meses["junho"][contador].produto.categoria = item.categoria
                            break

                if (dataset_vendas_meses["junho"][contador].produto.preco == 0):

                    for item in lista_de_emergencia_produtos:
                        if dataset_vendas_meses["junho"][contador].produto.id == item.id:
                            self.formatar_numero(item.preco)
                            dataset_vendas_meses["junho"][contador].produto.preco = item.preco

                            break

                precoDefinitivo = self.formatar_numero(dataset_vendas_meses["junho"][contador].produto.preco)
                dataset_vendas_meses["junho"][contador].produto.preco = precoDefinitivo
                dados_junho_tratados.append(dataset_vendas_meses["junho"][contador])

                if contador >= 360 and contador <= 419:
                    if (dataset_vendas_meses["julho"][contador].produto.nome == "" or dataset_vendas_meses["julho"][contador].produto.nome == " "):
                        for item in lista_de_emergencia_produtos:
                            if dataset_vendas_meses["julho"][contador].produto.id == item.id:
                                dataset_vendas_meses["julho"][contador].produto.nome = item.nome
                                break

                    if (dataset_vendas_meses["julho"][contador].produto.categoria == "" or
                            dataset_vendas_meses["julho"][contador].produto.categoria == " "):
                        for item in lista_de_emergencia_produtos:
                            if dataset_vendas_meses["julho"][contador].produto.id == item.id:
                                dataset_vendas_meses["julho"][contador].produto.categoria = item.categoria
                                break

                    if (dataset_vendas_meses["julho"][contador].produto.preco == 0):

                        for item in lista_de_emergencia_produtos:
                            if dataset_vendas_meses["julho"][contador].produto.id == item.id:
                                self.formatar_numero(item.preco)
                                dataset_vendas_meses["julho"][contador].produto.preco = item.preco

                                break

                    precoDefinitivo = self.formatar_numero(dataset_vendas_meses["julho"][contador].produto.preco)
                    dataset_vendas_meses["julho"][contador].produto.preco = precoDefinitivo
                    dados_julho_tratados.append(dataset_vendas_meses["julho"][contador])


                if contador >= 420 and contador <= 479:
                    if (dataset_vendas_meses["agosto"][contador].produto.nome == "" or dataset_vendas_meses["agosto"][contador].produto.nome == " "):
                        for item in lista_de_emergencia_produtos:
                            if dataset_vendas_meses["agosto"][contador].produto.id == item.id:
                                dataset_vendas_meses["agosto"][contador].produto.nome = item.nome
                                break

                    if (dataset_vendas_meses["agosto"][contador].produto.categoria == "" or
                            dataset_vendas_meses["agosto"][contador].produto.categoria == " "):
                        for item in lista_de_emergencia_produtos:
                            if dataset_vendas_meses["agosto"][contador].produto.id == item.id:
                                dataset_vendas_meses["agosto"][contador].produto.categoria = item.categoria
                                break

                    if (dataset_vendas_meses["agosto"][contador].produto.preco == 0):

                        for item in lista_de_emergencia_produtos:
                            if dataset_vendas_meses["agosto"][contador].produto.id == item.id:
                                self.formatar_numero(item.preco)
                                dataset_vendas_meses["agosto"][contador].produto.preco = item.preco

                                break

                    precoDefinitivo = self.formatar_numero(dataset_vendas_meses["agosto"][contador].produto.preco)
                    dataset_vendas_meses["agosto"][contador].produto.preco = precoDefinitivo
                    dados_agosto_tratados.append(dataset_vendas_meses["agosto"][contador])

                if contador >= 480 and contador <= 539:
                    if (dataset_vendas_meses["setembro"][contador].produto.nome == "" or dataset_vendas_meses["setembro"][contador].produto.nome == " "):
                        for item in lista_de_emergencia_produtos:
                            if dataset_vendas_meses["setembro"][contador].produto.id == item.id:
                                dataset_vendas_meses["setembro"][contador].produto.nome = item.nome
                                break

                    if (dataset_vendas_meses["setembro"][contador].produto.categoria == "" or
                            dataset_vendas_meses["setembro"][contador].produto.categoria == " "):
                        for item in lista_de_emergencia_produtos:
                            if dataset_vendas_meses["setembro"][contador].produto.id == item.id:
                                dataset_vendas_meses["setembro"][contador].produto.categoria = item.categoria
                                break

                    if (dataset_vendas_meses["setembro"][contador].produto.preco == 0):

                        for item in lista_de_emergencia_produtos:
                            if dataset_vendas_meses["setembro"][contador].produto.id == item.id:
                                self.formatar_numero(item.preco)
                                dataset_vendas_meses["setembro"][contador].produto.preco = item.preco

                                break

                    precoDefinitivo = self.formatar_numero(dataset_vendas_meses["setembro"][contador].produto.preco)
                    dataset_vendas_meses["setembro"][contador].produto.preco = precoDefinitivo
                    dados_setembro_tratados.append(dataset_vendas_meses["setembro"][contador])

                if contador >= 540 and contador <= 599:
                    if (dataset_vendas_meses["outubro"][contador].produto.nome == "" or dataset_vendas_meses["outubro"][contador].produto.nome == " "):
                        for item in lista_de_emergencia_produtos:
                            if dataset_vendas_meses["setembro"][contador].produto.id == item.id:
                                dataset_vendas_meses["setembro"][contador].produto.nome = item.nome
                                break

                    if (dataset_vendas_meses["setembro"][contador].produto.categoria == "" or
                            dataset_vendas_meses["setembro"][contador].produto.categoria == " "):
                        for item in lista_de_emergencia_produtos:
                            if dataset_vendas_meses["setembro"][contador].produto.id == item.id:
                                dataset_vendas_meses["setembro"][contador].produto.categoria = item.categoria
                                break

                    if (dataset_vendas_meses["setembro"][contador].produto.preco == 0):

                        for item in lista_de_emergencia_produtos:
                            if dataset_vendas_meses["setembro"][contador].produto.id == item.id:
                                self.formatar_numero(item.preco)
                                dataset_vendas_meses["setembro"][contador].produto.preco = item.preco

                                break

                    precoDefinitivo = self.formatar_numero(dataset_vendas_meses["setembro"][contador].produto.preco)
                    dataset_vendas_meses["setembro"][contador].produto.preco = precoDefinitivo
                    dados_setembro_tratados.append(dataset_vendas_meses["setembro"][contador])
            contador +=1    
    
        
        


        return dataset_vendas_meses


    

dados = Dados(2, 2, "a", 1)    
dados.montar_data_set()