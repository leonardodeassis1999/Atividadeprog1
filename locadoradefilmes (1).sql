-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 01/04/2026 às 03:16
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `locadoradefilmes`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `cliente`
--

CREATE TABLE `cliente` (
  `cadastro` int(11) NOT NULL,
  `cpf` bigint(11) DEFAULT NULL,
  `data_cadastro` date DEFAULT NULL,
  `historico_aluguel` date DEFAULT NULL,
  `endereco` text DEFAULT NULL,
  `nascimento` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `cliente`
--

INSERT INTO `cliente` (`cadastro`, `cpf`, `data_cadastro`, `historico_aluguel`, `endereco`, `nascimento`) VALUES
(1342678901, 10834412934, '0000-00-00', '0000-00-00', 'rua principal 01', '0000-00-00'),
(2147483647, 10835412938, '0000-00-00', '0000-00-00', 'rua principal 01', '0000-00-00');

-- --------------------------------------------------------

--
-- Estrutura para tabela `filme`
--

CREATE TABLE `filme` (
  `codigo` int(11) NOT NULL,
  `data_lancamento` date DEFAULT NULL,
  `genero` varchar(45) DEFAULT NULL,
  `reserva` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `filme`
--

INSERT INTO `filme` (`codigo`, `data_lancamento`, `genero`, `reserva`) VALUES
(1234567868, '1999-03-13', 'masculino', '2001-05-13'),
(2147483647, '1999-03-13', 'masculino', '2001-05-13');

-- --------------------------------------------------------

--
-- Estrutura para tabela `fornecedor`
--

CREATE TABLE `fornecedor` (
  `cnpj` int(11) NOT NULL,
  `contato` int(11) DEFAULT NULL,
  `preco` double DEFAULT NULL,
  `prazo_entrega` time DEFAULT NULL,
  `endereco` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `fornecedor`
--

INSERT INTO `fornecedor` (`cnpj`, `contato`, `preco`, `prazo_entrega`, `endereco`) VALUES
(1234567647, 2147483647, 1, '00:00:03', 'rua 02'),
(2147483647, 2147483647, 1, '00:00:03', 'rua 02');

-- --------------------------------------------------------

--
-- Estrutura para tabela `funcionario`
--

CREATE TABLE `funcionario` (
  `matiricula` int(11) NOT NULL,
  `funcao` varchar(45) DEFAULT NULL,
  `data_inicial` date DEFAULT NULL,
  `login` varchar(45) DEFAULT NULL,
  `carga_horaria` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `funcionario`
--

INSERT INTO `funcionario` (`matiricula`, `funcao`, `data_inicial`, `login`, `carga_horaria`) VALUES
(1987654321, 'operario', '1999-01-02', 'leoassis02@gmail.com', '00:00:03'),
(1987654371, 'operario', '1999-01-02', 'leoassis02@gmail.com', '03:06:54');

-- --------------------------------------------------------

--
-- Estrutura para tabela `locacao`
--

CREATE TABLE `locacao` (
  `contrato_locacao` int(11) NOT NULL,
  `data_locacao` date DEFAULT NULL,
  `matiricula` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `locacao`
--

INSERT INTO `locacao` (`contrato_locacao`, `data_locacao`, `matiricula`) VALUES
(2147483647, '1998-01-03', 1987654371);

-- --------------------------------------------------------

--
-- Estrutura para tabela `setor`
--

CREATE TABLE `setor` (
  `numero` int(11) NOT NULL,
  `genero` varchar(45) DEFAULT NULL,
  `vezes_alugado` int(11) DEFAULT NULL,
  `blueray` bit(1) DEFAULT NULL,
  `exemplares` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `setor`
--

INSERT INTO `setor` (`numero`, `genero`, `vezes_alugado`, `blueray`, `exemplares`) VALUES
(1209667555, 'feminino', 25, b'1', 302),
(2147483647, 'masculino', 14, b'1', 203);

-- --------------------------------------------------------

--
-- Estrutura para tabela `sistema`
--

CREATE TABLE `sistema` (
  `id_sistema` int(11) NOT NULL,
  `login` varchar(45) DEFAULT NULL,
  `data_acesso` date DEFAULT NULL,
  `locacao_inicio` date DEFAULT NULL,
  `locacao_fim` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `sistema`
--

INSERT INTO `sistema` (`id_sistema`, `login`, `data_acesso`, `locacao_inicio`, `locacao_fim`) VALUES
(946352398, 'leoassis@gmail.com', '1999-04-05', '2002-05-08', '2003-05-24'),
(2147483647, 'leoassis@gmail.com', '1999-04-05', '2002-05-08', '2003-05-24');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`cadastro`);

--
-- Índices de tabela `filme`
--
ALTER TABLE `filme`
  ADD PRIMARY KEY (`codigo`);

--
-- Índices de tabela `fornecedor`
--
ALTER TABLE `fornecedor`
  ADD PRIMARY KEY (`cnpj`);

--
-- Índices de tabela `funcionario`
--
ALTER TABLE `funcionario`
  ADD PRIMARY KEY (`matiricula`);

--
-- Índices de tabela `locacao`
--
ALTER TABLE `locacao`
  ADD PRIMARY KEY (`contrato_locacao`),
  ADD KEY `fkmatricula_funcionario` (`matiricula`);

--
-- Índices de tabela `setor`
--
ALTER TABLE `setor`
  ADD PRIMARY KEY (`numero`);

--
-- Índices de tabela `sistema`
--
ALTER TABLE `sistema`
  ADD PRIMARY KEY (`id_sistema`);

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `locacao`
--
ALTER TABLE `locacao`
  ADD CONSTRAINT `fkmatricula_funcionario` FOREIGN KEY (`matiricula`) REFERENCES `funcionario` (`matiricula`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
