defmodule GeneCompress do
    use Bitwise
    @doc """
        A = 0b00
        C = 0b01
        G = 0b10
        T = 0b11

    Convert number to string as binary:
        Integer.to_string(thenumber, 2)
    """

    @gene_bits = %{
        "A" => 0b00,
        "C" => 0b01,
        "G" => 0b10,
        "T" => 0b11,
    }
    # Map.fetch!(@gene_bits, "A")

    def compress_gene("A"), do: 0b00
    def compress_gene("C"), do: 0b01
    def compress_gene("G"), do: 0b10
    def compress_gene("T"), do: 0b11

    def compress(genes) do 
        String.graphemes(genes)  # -> transforma em lista uma string
        |> Enum.map(fn g -> compress_gene(g) end)
        |> Enum.reduce(fn x, 1 <<< 2, acc -> 
            acc <<< 2
            bor(x, acc) 
        end)
    end

    # def decompress(compressed_gene) do
        #bit_size(string)
    # end

end

original = "TAGGATCTCTCGAA"
IO.inspect GeneCompress.compress(original)

