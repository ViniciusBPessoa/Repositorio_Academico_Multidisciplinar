// Projeto 2 VA Arquitetura e Organização de Computadores - 2022.1
// Alunos: Vinícius Bezerra, Irlan Farias, Apolo Albuquerque, joão vitor castro
// Descrição do arquivo: Núcleo MIPS (Top-level)

module MIPS (clock, reset, PCs, ULSs, d_mens);  // Declaração dos inputs e outputs

	input wire clock;
	input wire reset;
	// saidas de demonstração
	output wire [31:0] PCs; //saida do pc
	output wire [31:0] ULSs; // saida da ula
	output wire [31:0] d_mens; // daida da d_men
	
	wire [31:0] con_PC_i_men; // cabo que liga PC a I_men
	wire [31:0] con_i_men_reg; // cabo que liga I_men a as outras partes do sistema (esse cabo sera separado em varias partes para alimentar diversas partes do sistema)
	
	PC pc_inst (.clock(clock), .nextPC(mux_PC_soma), .PC(con_PC_i_men)); // instancia de pc
	i_mem mem_inst (.address(con_PC_i_men), .i_out(con_i_men_reg)); // instancia de I-MEM
	
	// conjunto de cabos que comunicam ao processador as diferentes partes da instrução
	wire [5:0] op, funct; // cabo separando os bits para opcode e funct
	wire [4:0] rs, rt, rd, shf; // cabos para rs, rt, rd, shf
	
	// conjunto de cabos que ligam o processador a unidade de controle
	wire RegDst; 
	wire Br; 
	wire ALUSrc; 
	wire MemWrite; 
	wire MemRead; 
	wire MentoReg; 
	wire RegWrite; 
	wire [3:0] ALUOp; 
	// Fim das saidas da unidade de controle
	
	// cabos vinculados ao pc como somador por ex
	wire [31:0] soma_somador4;
	wire [31:0] extendido;
	wire [31:0] saida_somador_jumpr;
	wire [31:0] shift_2;
	
	
	// separador da instrução
	assign op = con_i_men_reg[31:26]; // separa os bits para op
	assign rs = con_i_men_reg[25:21]; // separa os bits para rs
	assign rt = con_i_men_reg[20:16]; // separa os bits para rt
	assign est = con_i_men_reg[15:0]; // separa os bits para extensor de sinal
	assign funct = con_i_men_reg[5:0]; // separa os bits para funct
	assign shf = con_i_men_reg [10:6]; // separa os bits para shf
	
	
	// cabos vinculados a memoria
	wire [31:0] soma_ou_memoria; 
	wire [31:0] saida_1_reg; // saida 1 da memoria
	wire [31:0] saida_2_reg; // saida 2 da meoria
	wire [31:0] saida_d_men; // saida da d_men
	wire [31:0] soma_lw; // saida dos registradores
	
	// cabos vinculados a alu
	wire [3:0] ctl_ula_ula;
	wire zero_flag; // cabo do 0 flag
	wire [31:0] result; // cabo com o resultado da ULA
	wire cabo_and; // cabo que leva o resultado do proximo PC
	
	
	// vem com as saidas do programa
	assign PCs = con_PC_i_men;
	assign ULSs = result;
	assign d_mens = saida_d_men;
	
	// instancia da unidade de controle
	d_mem d_mem (.Address(result), .WriteData(saida_2_reg), .ReadData(saida_d_men), .MemWrite(MemWrite), .MemRead(MemRead)); // instancia do modulo d_mem
	
	control unidade_de_controle (.opcode(op), .RegDst(RegDst), .Branch(Br), .ALUSrc(ALUSrc), .MemWrite(MemWrite), 
	.MemRead(MemRead), .MentoReg(MentoReg), .ALUOp(ALUOp), .RegWrite(RegWrite)); // instancia do modulo control(unidade de controle)
	
	somador_jump somador_jp (.soma_pc(soma_somador4), .ex_pc(shift_2), .po_jp(saida_somador_jumpr)); // instancia do modulo somador jump
	
	ula_ctrl ULA_contrl(.funct(funct), .ALUOp(ALUOp), .ALUControl(ctl_ula_ula)); // instancia do modulo ula_control
	
	ula ula (.In1(saida_1_reg), .In2(soma_ou_memoria), .OP(ctl_ula_ula), .shamt(shf), .Zero_flag(zero_flag), .result(result)); // instacia do modulo ula
	
	extensor_de_sinal ex_si (.entrada(est), .saida(extendido)); // sinal extendido para pc ainda vai passar por multiplexador
	
	somadorPC soma_1 (.nextPC(con_PC_i_men), .soma(soma_somador4)); // somador do pc
	
	regfile reg_inst (   // declaração do regfile com todos os inputs e outputs
  .ReadAddr1(rs),
  .ReadAddr2(rt),
  .ReadData1(saida_1_reg),
  .ReadData2(saida_2_reg),
  .Clock(clock),
  .WriteAddr(rd),
  .WriteData(soma_lw),
  .RegWrite(RegWrite),
  .Reset(reset));
	
	// Esse bloco contem todos os multiplexadores usados no modulo Top Level(Mips)
	
	assign rd = RegDst ? con_i_men_reg[15:11] : con_i_men_reg[20:16]; // mux que define se a se o dado vai ser gravado e onde
	
	
	assign mux_PC_soma = cabo_and ? saida_somador_jumpr : soma_somador4; // multiplexador que vai selecionar se a função é do tipo branche 
	
	assign soma_ou_memoria = ALUSrc ? extendido : saida_2_reg; // multiplexador que libera valor dos registradores ou da função
	
	assign soma_lw = MentoReg ? saida_d_men : result; // se vai escrever no banco de registradores o valor de d_mem ou ULA
	
	// essa parte altera o extensor de sinal fazendo shift left 2 
	
	assign shift_2 = extendido << 2; 
	
	// essa parte faz a porta end que seleciona se a instrução é dp tipo jump;
	assign cabo_and = Br & zero_flag; 
  
endmodule 
