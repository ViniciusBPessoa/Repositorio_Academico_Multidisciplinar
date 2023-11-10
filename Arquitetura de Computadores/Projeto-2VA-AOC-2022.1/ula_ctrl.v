// Projeto 2 VA Arquitetura e Organização de Computadores - 2022.1
// Alunos: Vinícius Bezerra, Irlan Farias, Apolo Albuquerque, joão vitor castro
// Descrição do arquivo: Unidade de controle da ULA

module ula_ctrl(
    input wire [5:0] funct,
    input wire [3:0] ALUOp,
    output reg [3:0] ALUControl
);

always @(*) begin
	 //AluOp aqui pega os 4 ultimos bits de Opcode, e para as instruções de lw e sw que fazem soma, coloquei default,
	 //pois o opcode delas usa mais do que 4 bits.
    case (ALUOp)
        4'b0000:
		      case(funct)
					6'b000000: ALUControl = 4'b1001; //sll -> Shift Left logico com shamt
					6'b000010: ALUControl = 4'b1010; //srl -> Shift Right logico com shamt
					6'b000011: ALUControl = 4'b1101; //sra -> Shift Right aritmetico com shamt
					6'b000100: ALUControl = 4'b0011; //sllv -> Shift Left Logical Variable
					6'b000110: ALUControl = 4'b0100; //srlv -> Shift Right Logical Variable
					6'b000111: ALUControl = 4'b0101; //srav -> Shift Right Arithmetic Variable
					6'b100000: ALUControl = 4'b0010; //add -> soma
					6'b100010: ALUControl = 4'b0110; //sub -> subtração
					6'b100100: ALUControl = 4'b0000; //and -> and
					6'b100101: ALUControl = 4'b0001; //or -> or
					6'b100110: ALUControl = 4'b1011; //xor -> xor
					6'b100111: ALUControl = 4'b1100; //nor -> nor
					6'b101010: ALUControl = 4'b0111; //slt -> Set On Less Than
					6'b101011: ALUControl = 4'b1111; //sltu -> Set On Less Than Unsigned
					default: ALUControl = 4'bxxxx; //don't care para instrução inválida
				endcase
		  4'b0100: ALUControl = 4'b0110; //beq -> subtração
		  4'b0101: ALUControl = 4'b1000; //bne -> sequencia especial para bne
		  4'b1000: ALUControl = 4'b0010; //addi -> soma
		  4'b1010: ALUControl = 4'b0111; //slti -> Set On Less Than Immediate
		  4'b1011: ALUControl = 4'b1111; //sltiu -> Set On Less Immediate Unsigned
		  4'b1100: ALUControl = 4'b0000; //andi -> and
		  4'b1101: ALUControl = 4'b0001; //ori -> or
		  4'b1110: ALUControl = 4'b1011; //xori -> xor
        default: ALUControl = 4'b0010; //default para as instruções de lw e sw que fazem soma
    endcase
end

endmodule
