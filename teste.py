import apache_beam as beam
from apache_beam.io import ReadFromText, WriteToText
from apache_beam.transforms import Map

# Defina a classe do pipeline
class WordCount(beam.DoFn):
    def process(self, element):
        words = element.split()
        return [(word, 1) for word in words]

# Crie um pipeline
with beam.Pipeline() as pipeline:
    # Leia o arquivo de texto
    lines = pipeline | ReadFromText('input.txt')

    # Conte as ocorrências de cada palavra
    word_counts = (
        lines
        | beam.ParDo(WordCount())
        | Map(lambda x: (x[0], sum(x[1])) if isinstance(x[1], list) else x)
    )

    # Formate e escreva os resultados no arquivo de saída
    word_counts | WriteToText('output.txt')
