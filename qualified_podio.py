def podio_olimpico(t1, t2, t3):
  tempos = [t1, t2, t3]
  tempos_ordenados = (sorted(tempos))
  return (
    f"1 - {tempos_ordenados[0]} minutos\n"
    f"2 - {tempos_ordenados[1]} minutos\n"
    f"3 - {tempos_ordenados[2]} minutos\n"
  )

podio_olimpico(6, 4, 8)