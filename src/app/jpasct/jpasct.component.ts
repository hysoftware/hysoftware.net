import { Component } from '@angular/core';

interface Source {
  key: string;
  value: string;
}

@Component({
  selector: 'app-jpasct',
  templateUrl: './jpasct.component.html',
  styleUrls: ['./jpasct.component.scss']
})
export class JPASCTComponent {
  columns = ['key', 'value'];
  src: Source[] = [
    {
      key: '名前',
      value: 'Hiroaki Yamamoto'
    },
    {
      key: '所在地、電話番号、及びメールアドレス',
      value: '請求書もしくは契約書にて記載'
    },
    {
      key: '運営統括責任者',
      value: 'Hiroaki Yamamoto'
    },
    {
      key: '追加手数料等の追加料金',
      value: 'エージェントによる仲介費用、銀行振込手数料、消費税、その他委託者起因による料金',
    },
    {
      key: '交換および返品（返金ポリシー）',
      value: `エージェントによる仲介の場合は、そのエージェントの返金ポリシーに準拠。
      それ以外は契約書に別途記載`
    },
    {
      key: '引渡(稼働開始)時期',
      value: `契約書に記載`
    },
    {
      key: '受け付け可能な決済手段',
      value: '請求書もしくは契約書にて記載'
    },
    {
      key: '決済期間',
      value: `エージェントによる仲介の場合は、そのエージェントのポリシーに準拠。
      それ以外は契約書に準ずる。`
    },
    {
      key: '販売価格',
      value: '商品の性質上、販売価格は契約時に決定。'
    }
  ]
}
