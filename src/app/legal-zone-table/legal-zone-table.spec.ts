import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LegalZoneTable } from './legal-zone-table';

describe('LegalZoneTable', () => {
  let component: LegalZoneTable;
  let fixture: ComponentFixture<LegalZoneTable>;
  const columns: string[] = [
    '名前', '所在地、電話番号、及びメールアドレス',
    '運営統括責任者', '追加手数料等の追加料金',
    '交換および返品（返金ポリシー）',
    '引渡(稼働開始)時期', '受け付け可能な決済手段',
    '決済期間', '販売価格'
  ];

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [LegalZoneTable]
    })
      .compileComponents();

    fixture = TestBed.createComponent(LegalZoneTable);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
  it('src has enough columns', () => {
    expect(component.src.map((el) => { return el.key; })).toStrictEqual(columns);
  });
});
